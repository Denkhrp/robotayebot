"""
Запусти ОДИН РАЗ локально, щоб отримати SESSION_STRING.
Telegram надішле код у застосунок (чат "Telegram")
"""
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID   = int(input("API_ID: ").strip())
API_HASH = input("API_HASH: ").strip()
PHONE    = input("Номер телефону (+380...): ").strip()

async def main():
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.start(phone=PHONE)
    session = client.session.save()
    print("\n" + "=" * 60)
    print("✅ SESSION_STRING:")
    print("=" * 60)
    print(session)
    print("=" * 60)
    print("⚠️  Нікому не передавай цей рядок — це доступ до твого акаунту!")
    await client.disconnect()

asyncio.run(main())
