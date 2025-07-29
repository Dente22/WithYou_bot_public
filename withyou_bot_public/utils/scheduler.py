# scheduler.py
# Планировщик задач для автоматического парсинга плейлиста

import schedule
import time

try:
    from utils.parser import parse_yandex_playlist
except ImportError:
    # 🔧 Заглушка, если нет настоящего парсера
    def parse_yandex_playlist(url):
        print(f"[ЗАГЛУШКА] Парсим плейлист: {url}")

def run_scheduler():
    # 🔗 Ссылка на открытый плейлист в Яндекс.Музыке
    playlist_url = "https://music.yandex.kz/users/gaponovdanylo/playlists/1005?utm_source=web&utm_medium=copy_link"

    # Первый запуск сразу
    parse_yandex_playlist(playlist_url)

    # Повторный запуск раз в сутки
    schedule.every(24).hours.do(lambda: parse_yandex_playlist(playlist_url))

    while True:
        schedule.run_pending()
        time.sleep(60)
