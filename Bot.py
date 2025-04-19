from telethon.sync import TelegramClient

# Substitua com sua API ID e API Hash
api_id = 20225004
api_hash = '8f4c78e858658cd2aa21967a087bf819'

# Substitua pelos seus IDs de canais
source_channel_id = 2590813877  # ID do canal de origem
destination_channel_id = 2656975250  # ID do canal de destino

# Inicia sessão com o nome 'session'
with TelegramClient('session', api_id, api_hash) as client:
    print("Conectado com sucesso!")

    # Itera pelas mensagens do canal de origem
    for message in client.iter_messages(source_channel_id):
        try:
            # Envia a mensagem para o canal de destino
            client.send_message(destination_channel_id, message.text)
            print(f"Mensagem enviada: {message.text}")
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
