from telebot import types
import random
from loader import bot
from utils.history import push

# 🗣 Подменю
communication_options = ["🧠 Мне нужно выговориться", "🫂 Просто будь рядом"]

# 🗣 Ответы
communication_answer = {
    "🧠 Мне нужно выговориться": [
        "Пиши. Всё, что хочешь. Я не буду перебивать, не буду судить. Просто выговорись.",
        "Я здесь. Даже если ты просто молчишь — я рядом. Но если хочешь вылить всё — сделай это. Мне можно."
    ],
    "🫂 Просто будь рядом": [
        "Без слов. Я рядом.",
        "Ты не один. Даже если всё молчит — я не молчу. Я с тобой."
    ]
}

# ▶ Обработчики
def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "💬 Просто поговорить")
    def handle_communication(message):
        user_last_topic[message.chat.id] = ("communication", None)
        push(message.chat.id, "communication")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*communication_options)
        markup.add("🏠 Меню")
        bot.send_message(
            message.chat.id,
            "Иногда просто нужно, чтобы кто-то был. Я буду. Что тебе ближе сейчас?",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in communication_answer)
    def handle_communication_option(message):
        user_last_topic[message.chat.id] = ("communication", message.text)
        push(message.chat.id, f"communication:{message.text}")

        response = random.choice(communication_answer[message.text])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")
        bot.send_message(message.chat.id, response, reply_markup=markup)

# 🔙 Откат
def handle_communication_step_back(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*communication_options)
    markup.add("🏠 Меню")
    bot.send_message(
        message.chat.id,
        "Иногда просто нужно, чтобы кто-то был. Я буду. Что тебе ближе сейчас?",
        reply_markup=markup
    )
