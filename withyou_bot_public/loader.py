# loader.py

from telebot import TeleBot

# 🔐 Вставьте свой токен ниже или загрузите из .env файла
# Пример безопасного варианта:
# import os
# TOKEN = os.getenv("BOT_TOKEN")

TOKEN = "YOUR_BOT_TOKEN_HERE"  # ← Замените на ваш токен

bot = TeleBot(TOKEN)
