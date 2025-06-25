from .database import get_connection

def get_channels():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM channels")
        return [row[0] for row in cursor.fetchall()]

def add_channel(username: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO channels (username) VALUES (?)", (username,))
        conn.commit()

def remove_channel(username: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM channels WHERE username=?", (username,))
        conn.commit()
