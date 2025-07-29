from telebot import types
import random
from utils.history import push

love_options = ["💔 Как пережить?", "💭 Я скучаю", "😓 Успокой меня"]

love_answers = {
    "💔 Как пережить?": [
        "Это больно. Это рушит. Но это не конец. Ты не стал хуже — ты стал глубже.",
        "Иногда то, что казалось вечным, заканчивается внезапно. Но ты всё равно достоин любви."
    ],
    "💭 Я скучаю": [
        "Скучать — это помнить. А помнить — значит, что это было важно.",
        "Пусть боль не станет якорем. Скука — не приговор, а свидетельство чувств."
    ],
    "😓 Успокой меня": [
        "Иногда любовь пугает. Но она не враг. Она приходит, когда мы перестаём ждать.",
        "Твоя вера не обязана быть вечной. Главное — не закрой сердце навсегда."
    ]
}

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "💔 Про любовь")
    def handle_love(message):
        user_last_topic[message.chat.id] = ("love", None)
        push(message.chat.id, "love")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*love_options)
        markup.add("🏠 Меню")
        bot.send_message(message.chat.id, "Выбери, что ближе к твоему состоянию:", reply_markup=markup)

    @bot.message_handler(func=lambda msg: msg.text in love_answers)
    def handle_love_option(message):
        user_last_topic[message.chat.id] = ("love", message.text)
        push(message.chat.id, f"love:{message.text}")

        response = random.choice(love_answers[message.text])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")
        bot.send_message(message.chat.id, response, reply_markup=markup)

def handle_love_step_back(bot, message):
    push(message.chat.id, "love")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*love_options)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(message.chat.id, "Выбери, что ближе к твоему состоянию:", reply_markup=markup)
