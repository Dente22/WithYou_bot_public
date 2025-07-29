# support_back_stub.py
# ⬅️ Заглушка для шага «Назад» в разделе поддержки

from telebot import types
from utils.history import push

# 🔙 Откат назад на главный экран поддержки
def handle_support_step_back(bot, message):
    push(message.chat.id, "support")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(
        message.chat.id,
        "[Stub] Если хочешь поговорить с человеком — напиши разработчику этого бота.",
        reply_markup=markup
    )

# 🔄 Переход на выбор в поддержке (письмо / прочитать)
def handle_support_step_back(bot, chat_id, subtopic):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📝 Написать письмо")
    markup.add("📩 Прочитать письмо")
    markup.add("🏠 Меню")
    bot.send_message(chat_id, "[Stub] Что хочешь сделать?", reply_markup=markup)
