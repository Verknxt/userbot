import asyncio
import platform
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    me = await bot.get_me()
    username = me.username
    firstname = me.first_name
    lastname = me.last_name
    if lastname is None:
        lastname = ""
    id = me.id
    userbot_python_version = platform.python_version()
    userbot_python_version_url = userbot_python_version.replace(".", "")
    await alive.edit("i'm alive!\n\n"
                                f"my name: [{firstname}{lastname}](tg://user?id={id})"
                                f"\ntelethon version: [{version.__version__}](https://pypi.org/project/Telethon/{version.__version__}/)"
                                f"\npython version: [{python_version()}](https://www.python.org/downloads/release/python-{userbot_python_version_url}/)")
