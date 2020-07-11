import asyncio
import platform
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

IMG = "https://srv-file20.gofile.io/download/lDPX8X/logo_photos_v2_x4.png"

@borg.on(admin_cmd("alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    me = await bot.get_me()
    username = me.username
    firstname = me.first_name
    lastname = me.last_name
    if lastname is None:
        lastname = ""
    id = me.id
    userbot_python_version = platform.python_version()
    userbot_python_version_url = userbot_python_version.replace(".", "")
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
        userbot_caption  = f"i'm alive!\n\n"
        userbot_caption += f"full name: [{firstname} {lastname}](tg://user?id={id})"   
        userbot_caption += f"\ntelethon version: [{version.__version__}](https://pypi.org/project/Telethon/{version.__version__}/)"
        userbot_caption += f"\npython version: [{python_version()}](https://www.python.org/downloads/release/python-{userbot_python_version_url}/)"
        await borg.send_file(alive.chat_id, IMG, caption=userbot_caption, reply_to=reply_to_id)