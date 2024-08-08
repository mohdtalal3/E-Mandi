import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  name TEXT NOT NULL,
                  region TEXT NOT NULL,
                  district TEXT NOT NULL,
                  tehsil TEXT NOT NULL,
                  phone TEXT NOT NULL,
                  picture BLOB)''')
    conn.commit()
    conn.close()


def init_grocery_db():
    conn = sqlite3.connect('grocery.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS groceries
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    season TEXT NOT NULL,
                    picture BLOB)''')
    conn.commit()
    conn.close()

def add_grocery(name, type, season, picture):
    conn = sqlite3.connect('grocery.db')
    c = conn.cursor()
    c.execute("INSERT INTO groceries (name, type, season, picture) VALUES (?, ?, ?, ?)",
              (name, type, season, picture))
    conn.commit()
    conn.close()

def get_groceries(type, search=None):
    conn = sqlite3.connect('grocery.db')
    c = conn.cursor()
    if search:
        c.execute("SELECT * FROM groceries WHERE type=? AND name LIKE ?", (type, f"%{search}%"))
    else:
        c.execute("SELECT * FROM groceries WHERE type=?", (type,))
    groceries = c.fetchall()
    conn.close()
    return groceries