import sqlite3
from datetime import datetime

DB_PATH = "letters.db"

# 🔧 Инициализация базы данных
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Таблица для личных писем (по user_id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS direct_letters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient_id INTEGER,
            sender_id INTEGER,
            text TEXT,
            date TEXT
        )
    """)

    # Таблица для писем по городу
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS city_letters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER,
            city TEXT,
            text TEXT,
            date TEXT
        )
    """)

    conn.commit()
    conn.close()

# 📩 Сохранить письмо конкретному пользователю
def save_direct_letter(recipient_id, sender_id, text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO direct_letters (recipient_id, sender_id, text, date)
        VALUES (?, ?, ?, ?)
    """, (recipient_id, sender_id, text, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()

# 📥 Получить последнее письмо для пользователя
def get_latest_direct_letter(recipient_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT sender_id, text, date
        FROM direct_letters
        WHERE recipient_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (recipient_id,))
    row = cursor.fetchone()
    conn.close()
    return row

# 🏙 Сохранить письмо по городу
def save_city_letter(sender_id, city, text):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO city_letters (sender_id, city, text, date)
        VALUES (?, ?, ?, ?)
    """, (sender_id, city, text, datetime.now().strftime('%Y-%m-%d %H:%M')))
    conn.commit()
    conn.close()

# 📜 Получить случайное письмо из города
def get_random_city_letter(city):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT text FROM city_letters
        WHERE city = ?
        ORDER BY RANDOM()
        LIMIT 1
    """, (city,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
