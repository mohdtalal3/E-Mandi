import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

def register_user(email, password, name, region, district, tehsil, phone, picture, user_type):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password, name, region, district, tehsil, phone, picture, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (email, hash_password(password), name, region, district, tehsil, phone, picture, user_type))
    conn.commit()
    conn.close()