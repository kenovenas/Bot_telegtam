from telethon import TelegramClient
import os

# Variáveis de ambiente para API
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Criar cliente Telegram
client = TelegramClient('bot', api_id, api_hash)

async def main():
    await client.start()
    print("Bot está rodando...")

with client:
    client.loop.run_until_complete(main())
