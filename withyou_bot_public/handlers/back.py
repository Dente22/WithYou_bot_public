from telebot import types
from utils.history import pop, clear
from handlers.support_back import handle_support_step_back

# ⬅ Обработка кнопки «Назад» и возврат к предыдущему состоянию
def handle(bot, user_last_topic, main_menu):
    @bot.message_handler(func=lambda msg: msg.text == "⬅ Назад")
    def go_back(message):
        topic_full = pop(message.chat.id)

        topic, subtopic = (topic_full.split(":", 1) + [None])[:2] if topic_full else (None, None)

        if topic == "love":
            from handlers.love import handle_love_step_back
            handle_love_step_back(bot, message.chat.id, subtopic)
        elif topic == "communication":
            from handlers.communication import handle_communication_step_back
            handle_communication_step_back(bot, message)
        elif topic == "panic":
            from handlers.panic import handle_panic_step_back
            handle_panic_step_back(bot, message)
        elif topic == "void":
            from handlers.void import handle_void_step_back
            handle_void_step_back(bot, message)
        elif topic == "music":
            from handlers.music import handle_music_step_back
            handle_music_step_back(bot, message)
        elif topic == "support":
            from handlers.support_back import handle_support_step_back
            handle_support_step_back(bot, message.chat.id, subtopic)
        elif topic == "find":
            from handlers.find import handle_find_step_back
            handle_find_step_back(bot, message)
        elif topic == "motivi":
            from handlers.motivi import handle_motivi_step_back
            handle_motivi_step_back(bot, message)
        else:
            bot.send_message(
                message.chat.id,
                "Ты уже в начале пути.",
                reply_markup=main_menu()
            )

    # 🏠 Обработка кнопки «Меню» — сброс истории и возврат в главное меню
    @bot.message_handler(func=lambda msg: msg.text == "🏠 Меню")
    def go_home(message):
        clear(message.chat.id)
        user_last_topic[message.chat.id] = (None, None)
        bot.send_message(
            message.chat.id,
            "Главное меню",
            reply_markup=main_menu(message.from_user.id)
        )
