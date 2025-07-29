# music_back_stub.py
# ⬅️ Заглушка для отката назад в музыкальном разделе

from telebot import types
from utils.history import push

def handle_music_step_back(bot, message):
    push(message.chat.id, "music")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💔 Любовь не взаимна", "🥀 Одиночество", "🌫 Пустота", "🎧 Песня дня")
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(
        message.chat.id,
        "[Stub] Возвращение в музыкальный раздел. Что чувствуешь сейчас?",
        reply_markup=markup
    )
