# panic_back_stub.py
# ⬅️ Заглушка для шага назад в разделе "Паника"

from telebot import types
from utils.history import push

def handle_panic_step_back(bot, message):
    push(message.chat.id, "panic")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("😦 Научи дышать", "🤕 Скажи что я не сломался")
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(
        message.chat.id,
        "[Stub] Держись. Я рядом. Что тебе нужно сейчас?",
        reply_markup=markup
    )
