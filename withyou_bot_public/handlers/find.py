from telebot import types
import random
from loader import bot
from utils.history import push

answers = {
    "🎭 Мне тяжело": [
        "О знакомое чувство, тяжести невообразимо огромной ответственности. Иногда так сильно давит, что не знаешь это от того что ты живой или нет",
        "Да... Чувство будто весь мир против тебя. Чувства переполнены, мысли запутаны, тело тяжёлое. Ужасное чувство, чувство тех кто добр к другим но не к себе. Я тебя понимаю, сам такой. И порой даже не знаю то ли это дар... Или проклятье",
        "Ты сильнее, чем думаешь. И я горжусь тобой, что ты здесь."
    ]
}

def handle(bot, user_last_topic):
    @bot.message_handler(func=lambda msg: msg.text == "🎭 Мне тяжело")
    def handle_find(message):
        user_last_topic[message.chat.id] = ("find", None)
        push(message.chat.id, "find")

        response = random.choice(answers[message.text])

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("🎧 Музыка", "🫂 Поговорить")
        markup.add("🏠 Меню")
        bot.send_message(
            message.chat.id,
            f"{response}\n\nХочешь, я включу тебе музыку или просто побуду рядом?",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text == "🎧 Музыка")
    def suggest_music(message):
        user_last_topic[message.chat.id] = ("find", "music")
        push(message.chat.id, "find:music")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")
        bot.send_message(
            message.chat.id,
            "📀 Вот мой плейлист для таких состояний:\nhttps://music.yandex.kz/users/gaponovdanylo/playlists/1005",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda msg: msg.text == "🫂 Поговорить")
    def talk_with_someone(message):
        user_last_topic[message.chat.id] = ("find", "talk")
        push(message.chat.id, "find:talk")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("⬅ Назад", "🏠 Меню")
        bot.send_message(
            message.chat.id,
            "Я рядом. Можешь просто писать, я отвечу.\n\n"
            "А если хочешь поговорить с живым человеком — напиши моему создателю @DiskusMS.",
            reply_markup=markup
        )

# 🔙 Откат на шаг назад
def handle_find_step_back(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎧 Музыка", "🫂 Поговорить")
    markup.add("🏠 Меню")
    bot.send_message(
        message.chat.id,
        "Хочешь, я включу тебе музыку или просто побуду рядом?",
        reply_markup=markup
    )
