# void_back_stub.py
# 🔙 Заглушка шага "назад" для состояния пустоты

from telebot import types
from utils.history import push

def handle_void_step_back(bot, message):
    push(message.chat.id, "void")  # [Stub] фиксируем возврат в тему
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("😒 Как вернуть себя?", "👀 Это пройдёт?")
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(
        message.chat.id,
        "[Stub] Это тяжёлое состояние... но выход всегда есть. Что тебе ближе сейчас?",
        reply_markup=markup
    )
