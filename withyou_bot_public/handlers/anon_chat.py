from loader import bot
from anon_storage import (
    add_to_waiting, get_partner, get_chat_partner,
    end_chat, is_in_chat
)
from telebot.types import ReplyKeyboardMarkup
from menu import main_menu


def handle(bot):
    # 🎭 Вход в анонимный чат
    @bot.message_handler(func=lambda msg: msg.text == "🎭 Анонимный чат")
    def start_anon_chat(message):
        user_id = message.chat.id

        if is_in_chat(user_id):
            bot.send_message(user_id, "Ты уже в анонимном чате. Напиши собеседнику или нажми 🔚 Завершить.")
            return

        warning = (
            "⚠️ *Важно!* Если у тебя скрыт профиль Telegram (нет username), "
            "бот не сможет отправить твой ник при приглашении в ЛС.\n\n"
            "🔹 Убедись, что у тебя указан username (пример: @yourname)."
        )
        bot.send_message(user_id, warning, parse_mode="Markdown")

        partner_id = get_partner(user_id)
        if partner_id:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add("🔚 Завершить", "📩 Приглашение в ЛС")
            bot.send_message(user_id, "Собеседник найден! Вы анонимны.", reply_markup=markup)
            bot.send_message(partner_id, "Собеседник найден! Вы анонимны.", reply_markup=markup)
        else:
            add_to_waiting(user_id)
            bot.send_message(user_id, "Ищу собеседника... Подожди немного.")

    # 🔚 Завершение общения
    @bot.message_handler(func=lambda msg: msg.text == "🔚 Завершить")
    def end_anon(message):
        user_id = message.chat.id
        partner_id = end_chat(user_id)

        if partner_id:
            end_msg = "❌ Общение завершено."
            bot.send_message(user_id, "Ты завершил общение.", reply_markup=main_menu(user_id))
            bot.send_message(partner_id, "Твой собеседник завершил общение.", reply_markup=main_menu(partner_id))
            bot.send_message(user_id, end_msg, reply_markup=main_menu(user_id))
        else:
            bot.send_message(user_id, "Ты сейчас ни с кем не общаешься.")

    # 📩 Приглашение в личные сообщения
    @bot.message_handler(func=lambda msg: msg.text == "📩 Приглашение в ЛС")
    def send_invite(message):
        user_id = message.chat.id
        partner_id = get_chat_partner(user_id)

        if partner_id:
            username = message.from_user.username
            text = (
                "🔔 Собеседник хочет перейти в ЛС.\n"
                f"🔗 Ник: @{username if username else 'недоступен'}"
            )
            bot.send_message(partner_id, text)

    # 📩 Пересылка сообщений между собеседниками
    @bot.message_handler(func=lambda msg: is_in_chat(msg.chat.id))
    def forward_message(message):
        sender = message.chat.id
        partner = get_chat_partner(sender)

        if partner:
            bot.send_message(partner, message.text)
