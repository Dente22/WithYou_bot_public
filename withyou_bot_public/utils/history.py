# history_stub.py
# 🧠 Заглушка для хранения истории действий пользователя (в памяти)

history_stack = {}

def push(chat_id, topic):
    """Сохранить шаг"""
    if chat_id not in history_stack:
        history_stack[chat_id] = []
    history_stack[chat_id].append(topic)
    print(f"[Stub] push: {topic} -> {chat_id}")

def pop(chat_id):
    """Вернуться на шаг назад"""
    if chat_id in history_stack and history_stack[chat_id]:
        topic = history_stack[chat_id].pop()
        print(f"[Stub] pop: {topic} <- {chat_id}")
        return topic
    return None

def clear(chat_id):
    """Очистить историю"""
    history_stack[chat_id] = []
    print(f"[Stub] clear history for {chat_id}")

def get_history(chat_id):
    """Получить стек истории"""
    return history_stack.get(chat_id, [])
