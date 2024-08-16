import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Create tables if they don't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  name TEXT NOT NULL,
                  region TEXT NOT NULL,
                  district TEXT NOT NULL,
                  tehsil TEXT NOT NULL,
                  phone TEXT NOT NULL,
                  picture BLOB,
                  user_type TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS groceries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  type TEXT NOT NULL,
                  season TEXT NOT NULL,
                  picture BLOB)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS daily_entries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  grocery_id INTEGER,
                  subtype TEXT,
                  quality TEXT,
                  price REAL,
                  video BLOB,
                  image BLOB,
                  date DATE,
                  type TEXT,
                  FOREIGN KEY (user_id) REFERENCES users(id),
                  FOREIGN KEY (grocery_id) REFERENCES groceries(id))''')
    
    conn.commit()
    conn.close()

def add_fake_users(num_users):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    for _ in range(num_users):
        c.execute('''INSERT INTO users (email, password, name, region, district, tehsil, phone, user_type)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (fake.email(), fake.password(), fake.name(),
                   fake.state(), fake.city(), fake.city_suffix(),
                   fake.phone_number(), random.choice(['employee'])))
    
    conn.commit()
    conn.close()

def add_fake_groceries():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    vegetables = [
        ("Tomato", "Summer", ["Cherry", "Beefsteak", "Roma"]),
        ("Cucumber", "Summer", ["English", "Persian", "Pickling"]),
        ("Carrot", "Winter", ["Nantes", "Chantenay", "Imperator"]),
        ("Spinach", "Winter", ["Savoy", "Flat-leaf", "Baby"]),
        ("Eggplant", "Summer", ["Italian", "Chinese", "Thai"]),
        ("Potato", "All Season", ["Russet", "Red", "Yukon Gold"]),
        ("Onion", "All Season", ["Red", "Yellow", "White"]),
        ("Cabbage", "Winter", ["Green", "Red", "Savoy"]),
        ("Cauliflower", "Winter", ["White", "Romanesco", "Purple"]),
        ("Bell Pepper", "Summer", ["Green", "Red", "Yellow"])
    ]
    
    fruits = [
        ("Apple", "Autumn", ["Gala", "Fuji", "Granny Smith"]),
        ("Banana", "All Season", ["Cavendish", "Red", "Plantain"]),
        ("Orange", "Winter", ["Navel", "Valencia", "Mandarin"]),
        ("Mango", "Summer", ["Alphonso", "Ataulfo", "Tommy Atkins"]),
        ("Strawberry", "Spring", ["June-bearing", "Everbearing", "Day-neutral"]),
        ("Watermelon", "Summer", ["Seedless", "Yellow", "Sugar Baby"]),
        ("Grape", "Autumn", ["Red Globe", "Thompson Seedless", "Concord"]),
        ("Pineapple", "Summer", ["Smooth Cayenne", "Queen", "Red Spanish"]),
        ("Peach", "Summer", ["Freestone", "Clingstone", "Donut"]),
        ("Kiwi", "Winter", ["Green", "Golden", "Hardy"])
    ]
    
    for grocery in vegetables + fruits:
        c.execute('''INSERT INTO groceries (name, type, season)
                     VALUES (?, ?, ?)''',
                  (grocery[0], "Vegetable" if grocery in vegetables else "Fruit", grocery[1]))
    
    conn.commit()
    conn.close()

def add_fake_daily_entries(num_entries):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Get all user IDs
    c.execute("SELECT id FROM users")
    user_ids = [row[0] for row in c.fetchall()]
    
    # Get all groceries with their subtypes
    c.execute("SELECT id, name, type FROM groceries")
    groceries = c.fetchall()
    
    vegetables = [
        ("Tomato", ["Cherry", "Beefsteak", "Roma"]),
        ("Cucumber", ["English", "Persian", "Pickling"]),
        ("Carrot", ["Nantes", "Chantenay", "Imperator"]),
        ("Spinach", ["Savoy", "Flat-leaf", "Baby"]),
        ("Eggplant", ["Italian", "Chinese", "Thai"]),
        ("Potato", ["Russet", "Red", "Yukon Gold"]),
        ("Onion", ["Red", "Yellow", "White"]),
        ("Cabbage", ["Green", "Red", "Savoy"]),
        ("Cauliflower", ["White", "Romanesco", "Purple"]),
        ("Bell Pepper", ["Green", "Red", "Yellow"])
    ]
    
    fruits = [
        ("Apple", ["Gala", "Fuji", "Granny Smith"]),
        ("Banana", ["Cavendish", "Red", "Plantain"]),
        ("Orange", ["Navel", "Valencia", "Mandarin"]),
        ("Mango", ["Alphonso", "Ataulfo", "Tommy Atkins"]),
        ("Strawberry", ["June-bearing", "Everbearing", "Day-neutral"]),
        ("Watermelon", ["Seedless", "Yellow", "Sugar Baby"]),
        ("Grape", ["Red Globe", "Thompson Seedless", "Concord"]),
        ("Pineapple", ["Smooth Cayenne", "Queen", "Red Spanish"]),
        ("Peach", ["Freestone", "Clingstone", "Donut"]),
        ("Kiwi", ["Green", "Golden", "Hardy"])
    ]
    
    subtypes_dict = {item[0]: item[1] for item in vegetables + fruits}
    
    for _ in range(num_entries):
        grocery = random.choice(groceries)
        grocery_id, grocery_name, grocery_type = grocery
        subtype = random.choice(subtypes_dict[grocery_name])
        
        c.execute('''INSERT INTO daily_entries 
                     (user_id, grocery_id, subtype, quality, price, date, type)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (random.choice(user_ids),
                   grocery_id,
                   subtype,
                   random.choice(['High', 'Medium', 'Low']),
                   round(random.uniform(10, 100), 2),
                   fake.date_between(start_date='-1y', end_date='today'),
                   random.choice(['distributor', 'mandi wala'])))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_fake_users(30)  # Add 50 fake users
    add_fake_groceries()  # Add predefined vegetables and fruits
    add_fake_daily_entries(1000)  # Add 1000 fake daily entries
    print("Fake data has been added to the database.")