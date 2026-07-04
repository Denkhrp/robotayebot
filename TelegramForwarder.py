import asyncio
import os
from telethon import TelegramClient, errors, events

# ─── Конфігурація ─────────────────────────────────────────────────────────────
API_ID       = os.environ["API_ID"]
API_HASH     = os.environ["API_HASH"]
PHONE        = os.environ["PHONE"]
SESSION      = os.environ.get("SESSION_STRING", "")

SOURCE_IDS   = [int(x.strip()) for x in os.environ["SOURCE_CHAT_IDS"].split(",")]
DEST_ID      = int(os.environ["DESTINATION_CHAT_ID"])
KEYWORDS_RAW = os.environ.get("KEYWORDS", "").strip()
KEYWORDS     = [k.strip().lower() for k in KEYWORDS_RAW.split(",")] if KEYWORDS_RAW else []

print(f"Джерела: {SOURCE_IDS}")
print(f"Призначення: {DEST_ID}")
print(f"Ключові слова: {KEYWORDS if KEYWORDS else 'ВСІ'}")

# ─── Клієнт ───────────────────────────────────────────────────────────────────
from telethon.sessions import StringSession

if SESSION:
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
else:
    client = TelegramClient("session_file", API_ID, API_HASH)

# ─── Хелпери ──────────────────────────────────────────────────────────────────
def build_message(message, source_chat):
    text = message.text or ""

    author_line = ""
    sender = message.sender
    if sender:
        if hasattr(sender, "username") and sender.username:
            author_line = f"\n👤 @{sender.username}"
        elif hasattr(sender, "first_name"):
            name = (sender.first_name or "").strip()
            if hasattr(sender, "last_name") and sender.last_name:
                name += f" {sender.last_name}"
            if name:
                author_line = f"\n👤 {name}"

    if hasattr(source_chat, "username") and source_chat.username:
        link = f"https://t.me/{source_chat.username}/{message.id}"
    else:
        chat_id = str(abs(source_chat.id))
        link = f"https://t.me/c/{chat_id}/{message.id}"

    return text + author_line + f"\n🔗 {link}"

# ─── Обробник нових повідомлень ───────────────────────────────────────────────
@client.on(events.NewMessage(chats=SOURCE_IDS))
async def handler(event):
    message = event.message
    if not message.text:
        return

    if KEYWORDS and not any(kw in message.text.lower() for kw in KEYWORDS):
        return

    source_chat = await event.get_chat()
    text_to_send = build_message(message, source_chat)

    try:
        await client.send_message(DEST_ID, text_to_send, link_preview=False)
        print(f"✅ Переслано з {source_chat.title} msg_id={message.id}")
    except Exception as e:
        print(f"❌ Помилка: {e}")

# ─── Запуск ───────────────────────────────────────────────────────────────────
async def main():
    await client.start(phone=PHONE)
    me = await client.get_me()
    print(f"✅ Авторизовано як: {me.first_name} ({me.phone})")
    print("🔍 Слухаю повідомлення...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
