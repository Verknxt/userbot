"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
     if not alive.text[0].isalpha() and alive.text[0] not in ("/", "#", "@", "!"):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("i'm alive!\n\n"
                     "telethon version: 1.14.0`\n`python version: 3.7.3")
