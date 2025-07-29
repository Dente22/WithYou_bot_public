from telebot import types
from utils.history import push

def handle_find_step_back(bot, message):
    push(message.chat.id, "find")  # сохраняем шаг, чтобы откат работал дальше

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎧 Музыка", "🫂 Поговорить")
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(message.chat.id, "Хочешь, я включу тебе музыку или просто побуду рядом?", reply_markup=markup)
