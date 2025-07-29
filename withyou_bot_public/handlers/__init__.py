# 📂 Импорт всех обработчиков по темам
from handlers.love import handle as handle_love
from handlers.communication import handle as handle_communication
from handlers.panic import handle as handle_panic
from handlers.motivi import handle as handle_motivi
from handlers.music import handle as handle_music
from handlers.find import handle as handle_find
from handlers.support import handle as handle_support
from handlers.void import handle as handle_void
from handlers.geo import handle as handle_geo
from handlers.anon_chat import handle as handle_anon_chat


# 📌 Главная функция регистрации
def register_all_handlers(bot, user_last_topic, main_menu):
    """
    Регистрирует все обработчики сообщений, включая тематики
    и специальные модули (гео, анонимный чат и т.д.)
    """
    handle_love(bot, user_last_topic)
    handle_communication(bot, user_last_topic)
    handle_panic(bot, user_last_topic)
    handle_motivi(bot, user_last_topic)
    handle_music(bot, user_last_topic)
    handle_find(bot, user_last_topic)
    handle_support(bot, user_last_topic)
    handle_void(bot, user_last_topic)
    handle_geo(bot, user_last_topic)
    handle_anon_chat(bot)  # 👥 Обрабатывает только bot
