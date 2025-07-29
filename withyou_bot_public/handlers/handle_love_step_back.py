def handle_love_step_back(bot, chat_id, last_subtopic):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*love_options)
    markup.add("⬅ Назад", "🏠 Меню")
    bot.send_message(chat_id, "Выбери, что ближе к твоему состоянию:", reply_markup=markup)
