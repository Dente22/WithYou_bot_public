# можно добавить в handlers/love.py или отдельный файл love_back.py
from telebot import types
from utils.history import push

def handle_love_step_back(bot, message):
    from handlers.love import love_options  # импортируем кнопки из основного модуля
    push(message.chat.id, "love")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*love_options)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(message.chat.id, "Возвращаю тебя к выбору. Что тебе ближе сейчас?", reply_markup=markup)
