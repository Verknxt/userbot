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
    userbot_python_version = platform.python_version()
    userbot_python_version_url = userbot_python_version.replace(".", "")
    await alive.edit("i'm alive!\n\n"
                                f"telethon version: [{version.__version__}](https://pypi.org/project/Telethon/{version.__version__}/)"
                                f"\npython version: [{python_version()}](https://www.python.org/downloads/release/python-{userbot_python_version_url}/)")
