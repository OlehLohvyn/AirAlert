import os
from dotenv import load_dotenv

# Завантаження змінних з .env файлу
load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE = os.getenv('PHONE')
CHAT_NAME = os.getenv('CHAT_NAME')

# Перевірка на наявність всіх необхідних змінних оточення
if not API_ID or not API_HASH or not PHONE or not CHAT_NAME:
    raise ValueError("Не всі змінні оточення визначені.")
