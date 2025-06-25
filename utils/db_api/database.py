import sqlite3

def get_connection():
    return sqlite3.connect("data/database.db")

def setup_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS channels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            code TEXT NOT NULL UNIQUE,
            views INTEGER DEFAULT 0
        )
        """)
        conn.commit()