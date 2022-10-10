import traceback
from telethon import TelegramClient, events
import asyncio
import time
import math
import random as rndm
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


# DESTINAZIONE  
prova_destinazione = '-1001880564029' # -791394339

# mto_siris

# bot_masterbet_id = tmb.TelegramBot(prova_destinazione, '5508923994:AAGJ1yG6pEr4mALgak9ChQ8apJqWgGP-0Gw')

# bot_mto_id = tmb.TelegramBot(, '')

# FONTI
fonte = '-1001638054050'

api_id = '16645531'
api_hash = '97be68b1fe05da4d818da2818bcb90d8'
phone = '+393333045341'

client = TelegramClient(phone, api_id, api_hash)


    # try:
    #     if chat.megagroup:
    #         groups.append(chat)
    # except:
    #     continue

chats = []
last_date = None
chunk_size = 200
groups = []

@client.on(events.NewMessage)
async def handle_new_message(event):
    print(event)
    destination = None
    result = await client(GetDialogsRequest(
        offset_id=0,
        offset_date=None,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
        ))
    chats.extend(result.chats)

    for chat in chats:
        # print(chat)
        try:
            if chat.id == 1880564029:
                destination = chat
        except:
            continue  

    if str(event.chat_id) == fonte: # sender_chat_id == prova_id
        if event.photo:
            image_base = event.message.media
            image_bytes = image_base.photo.bytes
        await client.forward_messages(destination, event.message)

        

client.start()
client.run_until_disconnected()
