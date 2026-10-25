# Telegram Channel Forwarder (robotayebot)

Автоматично пересилає повідомлення з публічних Telegram-каналів у ваш канал — з підписом автора та посиланням на джерело.

Проєкт початково розроблявся для мого брата, щоб автоматизувати процес пошуку вакансій у Львові. Замість ручного моніторингу десятків відкритих каналів, скрипт відстежує вказані цільові групи в реальному часі, фільтрує контент за ключовими словами (наприклад, "підробіток", "робота", "Львів") і миттєво пересилає всі релевантні пропозиції в один приватний чат. Це дозволяє зібрати всі можливості в єдиній зручній стрічці, зберігаючи оригінальні посилання та контакти авторів.

## Можливості

- Моніторить кілька каналів одночасно
- Фільтрація за ключовими словами
- Додає тег автора повідомлення (якщо є)
- Додає посилання на оригінальне повідомлення
- Готовий до деплою на Railway

## Як виглядає результат

```
Текст повідомлення з каналу...

👤 @author_username
🔗 https://t.me/channel_name/123
```

## Технології

- Python 3.x
- [Telethon](https://github.com/LonamiWebs/Telethon) — Telegram userbot бібліотека

## Швидкий старт

### 1. Клонуй репозиторій

```bash
git clone https://github.com/Denkhrp/robotayebot
cd robotayebot
```

### 2. Створи віртуальне середовище

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Отримай API ключі

1. Зайди на [my.telegram.org](https://my.telegram.org)
2. **API development tools** → створи новий застосунок
3. Збережи `API_ID` та `API_HASH`

### 4. Знайди ID каналів

```bash
python3 TelegramForwarder.py
# Вибери опцію 1 — List Chats
# Знайди потрібні канали у файлі chats_of_+380....txt
```

### 5. Отримай SESSION_STRING

```bash
python3 generate_session.py
# Введи API_ID, API_HASH, номер телефону
# Скопіюй SESSION_STRING що з'явиться
```

### 6. Налаштуй змінні середовища

Скопіюй `.env.example` у `.env` і заповни:

```bash
cp .env.example .env
```

```env
API_ID=123456
API_HASH=abcdef1234567890
PHONE=+380961234567
SESSION_STRING=довгий_рядок_сесії
SOURCE_CHAT_IDS=-1001234567890,-1009876543210
DESTINATION_CHAT_ID=-1001111111111
KEYWORDS=курс,долар
```

### 7. Запусти

```bash
python3 TelegramForwarder.py
```

##  Деплой на Railway(рекомендую)

1. Завантаж код на GitHub
2. Зайди на [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**
3. Додай змінні середовища з `.env` у розділі **Variables**
4. Railway автоматично запустить бота

## Змінні середовища

| Змінна | Опис | Приклад |
|--------|------|---------|
| `API_ID` | ID з my.telegram.org | `123456` |
| `API_HASH` | Hash з my.telegram.org | `abc123...` |
| `PHONE` | Номер телефону | `+380961234567` |
| `SESSION_STRING` | Рядок сесії з generate_session.py | `1BVts...` |
| `SOURCE_CHAT_IDS` | ID каналів-джерел через кому | `-1001234,-1005678` |
| `DESTINATION_CHAT_ID` | ID твого каналу | `-1001111111111` |
| `KEYWORDS` | Ключові слова через кому або порожньо | `курс,долар` |

## ⚠️ Важливо

- Ніколи не завантажуй `credentials.txt`, `*.session`, `.env` на GitHub
- `SESSION_STRING` — це доступ до твого акаунту, зберігай у таємниці
- Твій акаунт має бути підписаний на канали-джерела
- Твій акаунт має мати права адміністратора у цільовому каналі(канал, куди мають повідомлення пересилатися)


