from telethon.sync import TelegramClient

# Substitua com sua API ID e API Hash
api_id = 20225004
api_hash = '8f4c78e858658cd2aa21967a087bf819'

# IDs dos canais
canal_origem = 2590813877
canal_intermediario = 2656975250
# canal_final = ID_DO_CANAL_QUE_FALTA — você pode me passar esse se quiser 3 passos

with TelegramClient('session', api_id, api_hash) as client:
    print("Conectado com sucesso!")

    # Etapa 1: Copiar mensagens do canal de origem para o canal intermediário
    for message in client.iter_messages(canal_origem, limit=10):  # limite de testes
        try:
            if message.text:
                client.send_message(canal_intermediario, message.text)
                print(f"Mensagem enviada para intermediário: {message.text}")
        except Exception as e:
            print(f"Erro ao enviar para intermediário: {e}")

    # Etapa 2: Copiar mensagens do canal intermediário para outro canal
    for message in client.iter_messages(canal_intermediario, limit=10):
        try:
            if message.text:
                # Aqui você pode alterar para o canal_final se quiser outro destino
                client.send_message(canal_origem, message.text)
                print(f"Mensagem reenviada de volta: {message.text}")
        except Exception as e:
            print(f"Erro ao reenviar: {e}")
