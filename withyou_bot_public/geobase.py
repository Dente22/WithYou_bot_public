import sqlite3
from datetime import datetime

DB_PATH = "letters.db"  # или отдельную БД, если хочешь изолировать, например geo.db

def init_geo_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS geo_consent (
        user_id INTEGER PRIMARY KEY,
        consent INTEGER DEFAULT 0,
        first_visit INTEGER DEFAULT 1
    )
""")


    cur.execute("""
        CREATE TABLE IF NOT EXISTS geo_users (
            user_id INTEGER PRIMARY KEY,
            latitude REAL,
            longitude REAL,
            city TEXT,
            state TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_geo_consent(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO geo_consent (user_id, consent, first_visit)
        VALUES (?, 1, 0)
    """, (user_id,))
    conn.commit()
    conn.close()

def was_here_before(user_id: int) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT first_visit FROM geo_consent WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result is not None and result[0] == 0

def has_geo_consent(user_id: int) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT consent FROM geo_consent WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result and result[0] == 1

def save_user_location(user_id, lat, lon, city="Алматы", state="не указано"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO geo_users (user_id, latitude, longitude, city, state, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, lat, lon, city, state, datetime.now().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()

def get_city_by_user_id(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT city FROM geo_users WHERE user_id = ?", (user_id,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None


def get_nearby_users(current_user_id, limit=2):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT user_id, city, state, date
        FROM geo_users
        WHERE user_id != ?
        ORDER BY date DESC
        LIMIT ?
    """, (current_user_id, limit))
    rows = cur.fetchall()
    conn.close()

    users = []
    for row in rows:
        users.append({
            "user_id": row[0],
            "city": row[1],
            "state": row[2],
            "date": row[3]
        })
    return users

