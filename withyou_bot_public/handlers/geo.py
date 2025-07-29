from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from city_letters import save_direct_letter, get_latest_direct_letter
from geobase import has_geo_consent, save_geo_consent, save_user_location, get_nearby_users
from utils.history import push

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda m: m.text == "📍 Хочу найти кого-то рядом")
    def geo_entry(message: Message):
        from menu import main_menu
        user_id = message.from_user.id
        push(user_id, "geo:entry")

        if not has_geo_consent(user_id):
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.add("✅ Я согласен", "❌ Нет, спасибо")
            bot.send_message(
                message.chat.id,
                "🔒 *Мы уважаем твою приватность.*\n\n"
                "Чтобы найти людей рядом, нужно согласие на использование геолокации.",
                parse_mode="Markdown",
                reply_markup=markup
            )
            return

        bot.send_message(
            message.chat.id,
            "Ты уже дал согласие 🙌 Вот меню:",
            reply_markup=main_menu(user_id)
        )

    @bot.message_handler(func=lambda m: m.text == "✅ Я согласен")
    def consent_granted(message: Message):
        from menu import main_menu
        push(message.from_user.id, "geo:consent")
        save_geo_consent(message.from_user.id)
        bot.send_message(
            message.chat.id,
            "Спасибо! Теперь можно найти кого-то рядом 🙌",
            reply_markup=main_menu(message.from_user.id)
        )

    @bot.message_handler(func=lambda m: m.text == "❌ Нет, спасибо")
    def consent_denied(message: Message):
        from menu import main_menu
        push(message.from_user.id, "geo:deny")
        bot.send_message(
            message.chat.id,
            "Хорошо! Если передумаешь — просто нажми снова «📍 Хочу найти кого-то рядом»",
            reply_markup=main_menu(message.from_user.id)
        )

    @bot.message_handler(func=lambda m: m.text == "🔄 Обновить координаты")
    def update_location(message: Message):
        request_location(message)

    @bot.message_handler(content_types=['location'])
    def handle_location(message: Message):
        from menu import main_menu
        push(message.from_user.id, "geo:location")
        if message.location:
            save_user_location(
                message.from_user.id,
                message.location.latitude,
                message.location.longitude
            )
            bot.send_message(
                message.chat.id,
                "Координаты обновлены!",
                reply_markup=main_menu(message.from_user.id)
            )

    def request_location(message: Message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(KeyboardButton("📍 Отправить геолокацию", request_location=True))
        bot.send_message(
            message.chat.id,
            "Нажми кнопку ниже, чтобы отправить геолокацию",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda m: m.text == "👥 Люди рядом")
    def show_nearby_users(message: Message):
        push(message.from_user.id, "geo:nearby")
        users = get_nearby_users(message.from_user.id)
        if not users:
            bot.send_message(message.chat.id, "Пока никого рядом 😔")
            return

        for user in users:
            info = (
                f"🧍 Кто-то рядом\n"
                f"📍 Город: {user['city']}\n"
                f"💬 Состояние: {user['state']}\n"
                f"📅 Когда: {user['date']}"
            )
            inline = InlineKeyboardMarkup()
            inline.add(InlineKeyboardButton("✉ Написать письмо", callback_data=f"write_{user['user_id']}"))
            bot.send_message(message.chat.id, info, reply_markup=inline)

    @bot.callback_query_handler(func=lambda c: c.data.startswith("write_"))
    def handle_write_letter(call):
        recipient_id = int(call.data.split("_")[1])
        sender_id = call.from_user.id
        push(sender_id, f"geo:write:{recipient_id}")

        def save_and_notify(message: Message):
            text = message.text
            save_direct_letter(recipient_id, sender_id, text)
            bot.send_message(sender_id, "✅ Письмо отправлено!")
            bot.send_message(recipient_id, "📨 Ты получил новое письмо! Нажми «📩 Письмо от того кто рядом»")

        bot.send_message(call.message.chat.id, "✍ Напиши письмо:")
        bot.register_next_step_handler_by_chat_id(call.message.chat.id, save_and_notify)

    @bot.message_handler(func=lambda m: m.text == "📩 Письмо от того кто рядом")
    def read_direct_letter(message: Message):
        user_id = message.from_user.id
        push(user_id, "geo:read_letter")
        result = get_latest_direct_letter(user_id)

        if result:
            sender_id, text, date = result
            bot.send_message(
                message.chat.id,
                f"📬 Письмо для тебя:\n\n{text}\n\n🧍 Отправитель: кто-то рядом\n🕒 Дата: {date}"
            )
        else:
            bot.send_message(message.chat.id, "📭 Пока нет писем для тебя. Возможно, тебе ещё не ответили.")
