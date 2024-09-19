from telethon import TelegramClient
import asyncio
import os
from dotenv import load_dotenv

# Load .env file for API credentials
load_dotenv()

# API credentials from my.telegram.org or BotFather
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# Function to automate farming actions
async def auto_farm():
    try:
        # Start interaction with the target bot (e.g., Binance Moonbix bot)
        await client.send_message('@Binance_Moonbix_bot', '/start')
        print("Sent /start command to Binance Moonbix bot")

        await asyncio.sleep(5)  # Wait for a few seconds before sending the next command

        # Sending farming commands in a loop
        for i in range(10):  # Repeat farming command 10 times (adjustable)
            await client.send_message('@Binance_Moonbix_bot', '/farming')
            print(f"Farming command #{i+1} sent")
            await asyncio.sleep(60)  # Wait 60 seconds before sending the next command

    except Exception as e:
        print(f"Error occurred: {e}")

# Run the farming bot
with client:
    client.loop.run_until_complete(auto_farm())
