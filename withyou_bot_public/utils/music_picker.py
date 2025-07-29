# music_picker.py
# 🎵 Возвращает случайный трек из локального JSON

import json
import os
import random

TRACKS_FILE = "music_links.json"

def get_random_track() -> str:
    if not os.path.exists(TRACKS_FILE):
        return "⚠️ Плейлист пока не загружен. Попробуй позже."

    try:
        with open(TRACKS_FILE, "r", encoding="utf-8") as f:
            tracks = json.load(f)

        if not isinstance(tracks, list) or not tracks:
            return "📭 Плейлист пуст или повреждён."

        return random.choice(tracks)

    except Exception as e:
        print(f"[Ошибка чтения плейлиста]: {e}")
        return "❌ Ошибка при загрузке плейлиста. Попробуй позже."
