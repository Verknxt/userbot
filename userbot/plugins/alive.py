"""Check if userbot alive or not . """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

IMG = "https://i.postimg.cc/CKRjRwZ1/photo-2020-06-13-16-51-18.jpg"
alive_text = "i'm alive!\n\n"
alive_text += f"telethon version: `{version.__version__}`\n"
alive_text += f"python version: `{python_version()}`"


@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete()
    await borg.send_file(alive.chat_id, IMG, caption=alive_text)
