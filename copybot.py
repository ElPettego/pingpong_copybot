import telegram_message_bot as tmb
from telethon import TelegramClient, events

# DESTINAZIONE  
destinazione = '-1880564029' # -791394339

# FONTI -1638054050 -1638054050
fonte = '-1001638054050'

api_id = '16645531'
api_hash = '97be68b1fe05da4d818da2818bcb90d8'
phone = '+393333045341'

tmb_o = tmb.TelegramBot(destinazione, '5772267951:AAFo8gordFvJEyKGM4BkhVrqepMMgquFx_s')
client = TelegramClient(phone, api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_message(event):
    if str(event.chat_id) == fonte: # sender_chat_id == prova_id
        print(event)
        tmb_o.emit(str(event.message.message))
        if event.media != None:
            try:
                await event.download_media(file="prova.png")
                tmb_o.send_file('prova.png')
            except Exception:
                print('NO MEDIA IN THE MESSAGE')

        

client.start()
client.run_until_disconnected()
