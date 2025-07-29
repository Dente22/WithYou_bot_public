# anon_storage.py
# Простой in-memory storage для анонимного чата

# Пользователи, ожидающие собеседника
waiting_users = []

# Активные чаты (user_id: partner_id)
active_chats = {}


# Добавить пользователя в очередь ожидания
def add_to_waiting(user_id):
    if user_id not in waiting_users:
        waiting_users.append(user_id)


# Получить партнёра из очереди и начать чат
def get_partner(user_id):
    if user_id in waiting_users:
        waiting_users.remove(user_id)
    if waiting_users:
        partner_id = waiting_users.pop(0)
        active_chats[user_id] = partner_id
        active_chats[partner_id] = user_id
        return partner_id
    return None


# Получить ID собеседника пользователя
def get_chat_partner(user_id):
    return active_chats.get(user_id)


# Завершить чат для пользователя и удалить партнёра
def end_chat(user_id):
    partner = active_chats.pop(user_id, None)
    if partner:
        active_chats.pop(partner, None)
        return partner
    return None


# Проверить, находится ли пользователь в активном чате
def is_in_chat(user_id):
    return user_id in active_chats
