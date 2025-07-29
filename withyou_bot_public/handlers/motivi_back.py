from telebot import types
from utils.history import push
import random

answers = [
    "Ты — не ошибка. Ты процесс.",
    "Если ты открыл глаза сегодня — значит, ты уже победил.",
    "Однажды ты оглянешься и поймёшь — именно этот момент стал поворотным.",
    "Даже в самой чёрной луже может отражаться звезда. Просто продолжай идти.",
    "Ты — результат выживания. Не сломался. Уже это — подвиг."
]

def handle_motivi_step_back(bot, message):
    push(message.chat.id, "motivi")
    response = random.choice(answers)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(message.chat.id, response, reply_markup=markup)
