# support_stub.py
# 🤝 Заглушка для раздела поддержки: письмо незнакомцу

from telebot import types
from utils.history import push
from utils.letters_db import init_db, save_letter, get_random_letter, save_reply, get_letter_author

init_db()  # [Stub] инициализация БД писем

letter_options = ["📝 Написать письмо", "📩 Прочитать письмо"]
pending_reply = {}

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "ты хочешь поговоритьс живым человеком?")
    def handle_support(message):
        user_last_topic[message.chat.id] = ("support", None)
        push(message.chat.id, "support")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*letter_options)
        markup.add("⬅ Назад", "🏠 Меню")
        bot.send_message(message.chat.id, "[Stub] Что ты хочешь сделать?", reply_markup=markup)

    @bot.message_handler(func=lambda msg: msg.text == "📝 Написать письмо")
    def handle_write_letter(message):
        msg = bot.send_message(message.chat.id, "[Stub] Напиши письмо незнакомцу:")
        bot.register_next_step_handler(msg, save_user_letter)

    def save_user_letter(message):
        save_letter(message.text, message.chat.id)
        bot.send_message(message.chat.id, "[Stub] Письмо сохранено.")

    @bot.message_handler(func=lambda msg: msg.text == "📩 Прочитать письмо")
    def handle_read_letter(message):
        result = get_random_letter()
        if result:
            letter_id, content = result
            pending_reply[message.chat.id] = letter_id
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("✍ Ответить", "⬅ Назад", "🏠 Меню")
            bot.send_message(message.chat.id, f"[Stub] Письмо:\n\n{content}", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "[Stub] Писем пока нет.")

    @bot.message_handler(func=lambda msg: msg.text == "✍ Ответить")
    def handle_reply_prompt(message):
        if message.chat.id not in pending_reply:
            bot.send_message(message.chat.id, "[Stub] Нет письма для ответа.")
            return

        msg = bot.send_message(message.chat.id, "[Stub] Напиши ответ:")
        bot.register_next_step_handler(msg, lambda m: save_letter_reply(bot, m))

    def save_letter_reply(bot, message):
        letter_id = pending_reply.pop(message.chat.id, None)
        if letter_id:
            reply_text = message.text
            save_reply(letter_id, reply_text)

            author_chat_id = get_letter_author(letter_id)
            if author_chat_id:
                try:
                    bot.send_message(author_chat_id, f"[Stub] Кто-то ответил на твоё письмо:\n\n{reply_text}")
                except Exception as e:
                    print(f"[!] Ошибка отправки ответа: {e}")

            bot.send_message(message.chat.id, "[Stub] Ответ отправлен.")
        else:
            bot.send_message(message.chat.id, "[Stub] Ошибка при отправке.")
