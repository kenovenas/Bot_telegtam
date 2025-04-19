from telethon import TelegramClient
from config import API_ID, API_HASH  # Importando as credenciais de config.py

# Nome da sessão
client = TelegramClient('my_session', API_ID, API_HASH)

async def main():
    # Conectar ao Telegram
    await client.start()
    print("Conectado ao Telegram!")

# Rodar o script
with client:
    client.loop.run_until_complete(main())
