from loader import bot
from menu import main_menu, feelings_menu, talk_menu
from handlers import register_all_handlers
from handlers.back import handle as handle_back
from datetime import datetime
from threading import Thread

# 🔧 Заглушка: функция периодических задач
from utils.scheduler import run_scheduler

# 📦 Заглушка: импорт парсера (автоматический запуск при импорте)
# from utils import parser

# 📌 Заглушка: инициализация гео-базы и базы писем
def init_geo_db():
    # Реализуй при необходимости: создаёт таблицы координат и гео-согласий
    pass

def init_db():
    # Реализуй при необходимости: создаёт таблицу писем и другие сущности
    pass

# 📌 Заглушка: если есть geo-обработчик
def handle_geo(bot, user_last_topic):
    # Реализуй при необходимости: добавь обработку координат
    pass

# 📌 Запускаем планировщик в отдельном потоке
Thread(target=run_scheduler).start()

# 📌 Инициализация баз данных
init_db()
init_geo_db()

# 📌 Словарь для хранения последней темы пользователя
user_last_topic = {}

# 📌 Регистрируем обработчики
register_all_handlers(bot, user_last_topic, main_menu())
handle_back(bot, user_last_topic, main_menu)
handle_geo(bot, user_last_topic)

# 🔘 Меню чувств
@bot.message_handler(func=lambda msg: msg.text == "🧠 Чувства")
def show_feelings_menu(message):
    bot.send_message(message.chat.id, "Что ты чувствуешь сейчас?", reply_markup=feelings_menu())

# 🔘 Меню общения
@bot.message_handler(func=lambda msg: msg.text == "🫂 Пообщаться")
def show_talk_menu(message):
    bot.send_message(message.chat.id, "Как ты хочешь поговорить?", reply_markup=talk_menu())

# 🟢 Старт команды
@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = main_menu()
    bot.send_message(message.chat.id, "Привет! Я рядом.", reply_markup=markup)

# ▶️ Основной запуск
if __name__ == "__main__":
    print(f"🤖 Бот запущен! ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    init_db()
    bot.infinity_polling()
