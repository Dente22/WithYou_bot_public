from telebot import types
from utils.history import push

# Подменю (можно дублировать из основного файла или импортировать)
communication_options = ["🧠 Мне нужно выговориться", "🫂 Просто будь рядом"]

def handle_communication_step_back(bot, message):
    push(message.chat.id, "communication")  # возвращаемся на шаг назад
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*communication_options)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(message.chat.id, "Давай вернёмся к началу. Что тебе ближе сейчас?", reply_markup=markup)
