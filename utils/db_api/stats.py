from .database import get_connection

def increment_view(code: str):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO stats (code, views) VALUES (?, 0)", (code,))
        cur.execute("UPDATE stats SET views = views + 1 WHERE code = ?", (code,))
        conn.commit()

def get_top_films(limit=10):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT code, views FROM stats ORDER BY views DESC LIMIT ?", (limit,))
        return cur.fetchall()
