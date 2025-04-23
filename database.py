import sqlite3

def connect_db():
    return sqlite3.connect("users.db", check_same_thread=False)

def create_users_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            password TEXT,
            is_premium INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, name, email, hashed_password, is_premium=0):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (username, name, email, hashed_password, is_premium))
    conn.commit()
    conn.close()

def get_user(username):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    return c.fetchone()
