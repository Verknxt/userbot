import asyncio
import platform
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname


@command(pattern="^.id")
async def _(event):
    if event.fwd_from:
        return
    id = event.chat_id
    await event.edit("`{id}`")