# motivi_back.py
# ⬅️ Заглушка для мотивационного раздела (необязательная)

from telebot import types
from utils.history import push

def handle_motivi_step_back(bot, message):
    push(message.chat.id, "motivi")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕯 Мотивация \\ фраза")
    markup.add("🏠 Меню")
    bot.send_message(
        message.chat.id,
        "Хочешь услышать что-то, что придаст тебе сил? Я рядом.",
        reply_markup=markup
    )
