import asyncio
import platform
from telethon import events
from platform import uname
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

USERBOT_IMG = "https://telegra.ph/file/d88964c031e2cff68bcb3.png"

@borg.on(admin_cmd("alive$"))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    me = await bot.get_me()
    username = me.username
    firstname = me.first_name
    lastname = me.last_name
    if lastname is None:
        lastname = ""
    id = me.id
    userbot_python_version = platform.python_version()
    userbot_python_version_url = userbot_python_version.replace(".", "")
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if USERBOT_IMG:
         userbot_caption  = "i'm alive!\n\n"
         userbot_caption += f"full name: [{firstname} {lastname}](tg://user?id={id})"   
         userbot_caption += f"\ntelethon version: [{version.__version__}](https://pypi.org/project/Telethon/{version.__version__}/)"
         userbot_caption += f"\npython version: [{python_version()}](https://www.python.org/downloads/release/python-{userbot_python_version_url}/)"
         await alive.delete()
         await borg.send_file(alive.chat_id, USERBOT_IMG, caption=userbot_caption)
    else:
        await alive.edit("i'm alive!\n\n"
                         f"full name: [{firstname} {lastname}](tg://user?id={id})" 
                         f"\ntelethon version: [{version.__version__}](https://pypi.org/project/Telethon/{version.__version__}/)"
			             f"\npython version: [{python_version()}](https://www.python.org/downloads/release/python-{userbot_python_version_url}/)"
                        )         