# panic_stub.py
# ⛈ Заглушка для раздела "Паника"

from telebot import types
import random
from utils.history import push

# 🔘 Возможные варианты и ответы
answers = {
    "🌪 У меня паника": [
        "[Stub] Паника — это временно. Ты не один.",
        "[Stub] Представь, что кто-то рядом. Это я.",
        "[Stub] Ты жив. Ты дышишь. Ты справляешься."
    ]
}

panic_options = ["😦 Научи дышать", "🤕 Скажи что я не сломался"]

panic_answer = {
    "😦 Научи дышать": [
        "[Stub] Вдох на 4 секунды… Задержка… Выдох на 4 секунды… Повтори.",
        "[Stub] Возьми подушку, обними. Представь, что рядом человек. Дыши.",
        "[Stub] Дыхание — это якорь. Медленно вдохни, задержи, выдохни. Повтори."
    ],
    "🤕 Скажи что я не сломался": [
        "[Stub] Ты не сломался. Ты просто устал. И это нормально.",
        "[Stub] Раз ты пишешь — ты уже борешься. Это важно.",
        "[Stub] Сломаться — это когда сдался. А ты всё ещё здесь."
    ]
}

# 🔁 Основной обработчик
def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "🌪 У меня паника")
    def handle_panic(message):
        user_last_topic[message.chat.id] = ("panic", None)
        push(message.chat.id, "panic")

        response = random.choice(answers[message.text])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*panic_options)
        markup.add("🏠 Меню")

        bot.send_message(
            message.chat.id,
            f"{response}\n\n[Stub] Что тебе нужно прямо сейчас?",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text in panic_answer)
    def handle_panic_option(message):
        user_last_topic[message.chat.id] = ("panic", message.text)
        push(message.chat.id, f"panic:{message.text}")

        response = random.choice(panic_answer[message.text])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")

        bot.send_message(message.chat.id, response, reply_markup=markup)

# 🔙 Шаг назад
def handle_panic_step_back(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*panic_options)
    markup.add("🏠 Меню")
    bot.send_message(message.chat.id, "[Stub] Что тебе нужно прямо сейчас?", reply_markup=markup)
