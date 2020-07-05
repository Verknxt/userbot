import asyncio
import platform
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname


@command(outgoing=True, pattern="^.id$")
async def chatid(id):
    chat_id = event.chat_id
    await id.edit(f"{chat_id}")