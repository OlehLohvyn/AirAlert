# telegram_parser.py
from telethon import TelegramClient, events
import config


class TelegramMessageParser:
    def __init__(self):
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH
        self.phone = config.PHONE
        self.client = None
        self.chat_name = config.CHAT_NAME  # Ваша назва чату або каналу
        self.last_message = None  # Змінна для збереження останнього повідомлення

    async def initialize(self):
        """Почати роботу з клієнтом Telegram"""
        if not self.api_id or not self.api_hash:
            raise ValueError("API_ID або API_HASH не задано.")

        self.client = TelegramClient('session_name', self.api_id, self.api_hash)
        await self.client.connect()

        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone)
            await self.client.sign_in(self.phone)

        print("Підключення до Telegram успішно здійснено!")

    async def start_parsing_messages(self):
        """Почати парсинг повідомлень з чату або каналу"""
        try:
            # Отримуємо чат або канал за іменем
            entity = await self.client.get_entity(self.chat_name)
            print(
                f"Розпочато парсинг повідомлень з чату/каналу: {entity.title if hasattr(entity, 'title') else self.chat_name}")

            # Отримуємо повідомлення з чату
            @self.client.on(events.NewMessage(chats=entity))
            async def handler(event):
                # Зберігаємо останнє повідомлення
                self.last_message = event.message.text
                print(f"Новине повідомлення від {event.message.sender_id}: {event.message.text}")

            # Чекаємо на нові повідомлення
            print("Очікування нових повідомлень...")
            await self.client.run_until_disconnected()

        except Exception as e:
            print(f"Помилка при отриманні чату: {e}")

        # Повертаємо останнє повідомлення після завершення
        return self.last_message
