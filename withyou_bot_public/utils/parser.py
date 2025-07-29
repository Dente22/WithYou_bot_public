# parser.py
# 📥 Парсит ссылки из плейлиста Яндекс.Музыки

import requests
from bs4 import BeautifulSoup
import os

def parse_yandex_playlist(playlist_url: str, save_path: str = "utils/parsed_tracks.txt"):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(playlist_url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        track_links = []

        for link in soup.select("a.d-link.deco-link"):
            href = link.get("href")
            if href and "/album/" in href:
                full_link = f"https://music.yandex.kz{href}"
                if full_link not in track_links:
                    track_links.append(full_link)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            for link in track_links:
                f.write(link + "\n")

        print(f"[🎵] Обновлено {len(track_links)} ссылок из плейлиста.")
    except Exception as e:
        print(f"[⚠️] Ошибка при парсинге: {e}")
