import sqlite3

def connect():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password))

    conn.commit()
    conn.close()


def get_user(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()

    conn.close()
    return user