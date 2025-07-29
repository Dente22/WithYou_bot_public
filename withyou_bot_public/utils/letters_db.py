# letters_db_stub.py
# 📝 Заглушка для писем и ответов (без реальной БД)

_fake_db = {
    "letters": [],
    "next_id": 1
}

def init_db():
    print("[Stub] База данных писем инициализирована.")

def save_letter(content, chat_id):
    letter = {
        "id": _fake_db["next_id"],
        "content": content,
        "reply": None,
        "chat_id": chat_id
    }
    _fake_db["letters"].append(letter)
    _fake_db["next_id"] += 1
    print(f"[Stub] Письмо сохранено: {content}")

def get_random_letter():
    available = [l for l in _fake_db["letters"] if l["reply"] is None]
    if not available:
        return None
    letter = random.choice(available)
    return (letter["id"], letter["content"])

def save_reply(letter_id, reply_text):
    for letter in _fake_db["letters"]:
        if letter["id"] == letter_id:
            letter["reply"] = reply_text
            print(f"[Stub] Ответ сохранён для письма #{letter_id}")
            return

def get_letter_author(letter_id):
    for letter in _fake_db["letters"]:
        if letter["id"] == letter_id:
            return letter["chat_id"]
    return None
