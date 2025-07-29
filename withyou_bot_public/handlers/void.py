# void_stub.py
# 🌫 Заглушка: реакция на чувство "ничего не чувствую"

from telebot import types
import random
from utils.history import push
from loader import bot

answers = {
    "🌫 Я ничего не чувствую": [
        "[Stub] Пустота... но это перезагрузка. Всё вернётся.",
        "[Stub] Просто побыть — уже достаточно.",
        "[Stub] Иногда мы перезагружаемся. Не вини себя за это."
    ]
}

feeling_options = ["😒 Как вернуть себя?", "👀 Это пройдёт?"]

feeling_answer = {
    "😒 Как вернуть себя?": [
        "[Stub] Всё вернётся: цвета, запахи, музыка. Ты не потерян.",
        "[Stub] Ты в режиме ожидания. Всё будет хорошо."
    ],
    "👀 Это пройдёт?": [
        "[Stub] Да. Даже если ты не веришь — это пройдёт.",
        "[Stub] Пустота — это не ты. Это временно."
    ]
}

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "🌫 Я ничего не чувствую")
    def handle_feeling(message):
        user_last_topic[message.chat.id] = ("void", None)
        push(message.chat.id, "void")
        response = random.choice(answers[message.text])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*feeling_options)
        markup.add("🏠 Меню")

        bot.send_message(
            message.chat.id,
            f"{response}\n\nЧто из этого тебе сейчас ближе?",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in feeling_answer)
    def handle_feeling_option(message):
        user_last_topic[message.chat.id] = ("void", message.text)
        push(message.chat.id, f"void:{message.text}")
        response = random.choice(feeling_answer[message.text])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")

        bot.send_message(message.chat.id, response, reply_markup=markup)

# ⬅️ Шаг назад
def handle_void_step_back(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*feeling_options)
    markup.add("🏠 Меню")
    bot.send_message(message.chat.id, "[Stub] Что из этого тебе сейчас ближе?", reply_markup=markup)
