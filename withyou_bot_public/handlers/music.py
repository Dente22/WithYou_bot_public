# music_stub.py
# 🎵 Заглушка для музыкального раздела бота поддержки

from telebot import types
from utils.history import push
# from utils.music_picker import get_random_track

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "📀Песня")
    def handle_music(message):
        user_last_topic[message.chat.id] = ("music", None)
        push(message.chat.id, "music")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("💔 Любовь не взаимна", "🥀 Одиночество", "🌫 Пустота", "🎧 Песня дня")
        markup.add("🏠 Меню")

        bot.send_message(
            message.chat.id,
            "[Stub] Музыкальный раздел. Выбери состояние, и я подберу плейлист.",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in [
        "💔 Любовь не взаимна", "🥀 Одиночество", "🌫 Пустота", "🎧 Песня дня"
    ])
    def suggest_music(message):
        user_last_topic[message.chat.id] = ("music", message.text)
        push(message.chat.id, f"music:{message.text}")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")

        bot.send_message(
            message.chat.id,
            f"[Stub] Плейлист для настроения: {message.text}",
            reply_markup=markup
        )

def handle_music_step_back(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("💔 Любовь не взаимна", "🥀 Одиночество", "🌫 Пустота", "🎧 Песня дня")
    markup.add("🏠 Меню")
    bot.send_message(
        message.chat.id,
        "[Stub] Возвращение в музыкальный раздел. Что чувствуешь сейчас?",
        reply_markup=markup
    )
