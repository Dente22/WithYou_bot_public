from telebot import types
from loader import bot
from telebot.types import ReplyKeyboardMarkup

# 📌 Заглушка: импорт своей функции проверки гео-согласия
# Удали эту заглушку и вставь свою функцию, если она есть
def has_geo_consent(user_id):
    # Здесь должна быть твоя логика, возвращающая True/False
    return False

# 🔘 Главное меню
def main_menu(user_id=None):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    # Основные кнопки
    markup.add("🧠 Чувства", "🫂 Пообщаться")
    markup.add("📀Песня")

    # Гео-кнопки, если согласие получено
    if user_id and not has_geo_consent(user_id):
        markup.add("📍 Хочу найти кого-то рядом")
    elif user_id and has_geo_consent(user_id):
        markup.add("👥 Люди рядом", "🔄 Обновить координаты", "📩 Письмо от того кто рядом", "🎭 Анонимный чат")

    return markup

# 🔘 Меню «🧠 Чувства»
def feelings_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("💔 Про любовь", "🎭 Мне тяжело")
    markup.add("🌫 Я ничего не чувствую", "🌪 У меня паника")
    markup.add("🏠 Меню")
    return markup

# 🔘 Меню «🫂 Поговорить»
def talk_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add("💬 Просто поговорить", "📝 Написать письмо", "📩 Прочитать письмо")
    markup.add("🏠 Меню")
    return markup

# 🔘 Универсальное меню назад
def back_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⬅ Назад")
    return markup
