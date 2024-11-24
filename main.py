from telethon import TelegramClient, events
from voice import say
from dotenv import load_dotenv
import os

load_dotenv()

# Load API credentials and settings from environment variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
chat_name = os.getenv("CHAT_NAME")


# Define chat and keywords for message filtering
chat_name = 'kievinfo_kyiv'  # Target chat to monitor
keywords = ['Київ', 'Київщина', "Київщину", "Києва", 'Київ.', 'Київщина.', "Київщину.", "Києва."]  # Keywords to look for

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Main function to start the client and monitor messages
async def main():
    await client.start(phone=phone)  # Authenticate and connect to Telegram

    # Event handler: triggered when a new message is received in the specified chat
    @client.on(events.NewMessage(chats=chat_name))
    async def handler(event):
        message_text = event.message.message  # Get the text of the incoming message
        # Check if the message contains any of the specified keywords
        if any(keyword.lower() in message_text.lower() for keyword in keywords):
            print(f"Знайдено повідомлення: {message_text}")  # Log the matching message
            say(message_text)  # Perform an action (e.g., text-to-speech)

    print("Парсинг почався...")  # Notify the user that monitoring has started
    await client.run_until_disconnected()  # Keep the client running to listen for messages

# Run the client and execute the main function
with client:
    client.loop.run_until_complete(main())
