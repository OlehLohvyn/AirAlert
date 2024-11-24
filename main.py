# main.py
import asyncio
from telegram_parser import TelegramMessageParser

async def run_parser():
    parser = TelegramMessageParser()  # Ініціалізуємо парсер
    await parser.initialize()  # Підключення до Telegram
    last_message = await parser.start_parsing_messages()  # Починаємо парсинг
    if last_message:
        print(f"Останнє повідомлення: {last_message}")
    else:
        print("Не було отримано повідомлення.")

if __name__ == "__main__":
    asyncio.run(run_parser())  # Запуск парсера через asyncio
