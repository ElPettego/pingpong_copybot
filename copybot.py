from io import BytesIO
from tkinter import Image
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

# FONTI -1638054050
fonte1 = '-1001638054050'
fonte2 = '-1001896425972'

api_id = '16645531'
api_hash = '97be68b1fe05da4d818da2818bcb90d8'
phone = '+393333045341'

client = TelegramClient(phone, api_id, api_hash)


    # try:
    #     if chat.megagroup:
    #         groups.append(chat)
    # except:
    #     continue
photo = None
chats = []
last_date = None
chunk_size = 200
groups = []

@client.on(events.NewMessage)
async def handle_new_message(event):
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
    # print(str(event.chat_id))
    if str(event.chat_id) == fonte1 or str(event.chat_id) == fonte2: # sender_chat_id == prova_id
        print(event)
        await client.send_message(destination, str(event.message.message))
        if event.media != None:
            try:
                await event.download_media(file="prova.png")
                await client.send_file(destination, "prova.png")
            except Exception:
                print('NO MEDIA IN THE MESSAGE')

        

client.start()
client.run_until_disconnected()
