from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import datetime
import time
#from userbot.utils import admin_cmd
from userbot.events import register 
from userbot import bot, CMD_HELP
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import glob
import os
try:
 import instantmusic , subprocess
except:
 os.system("pip install instantmusic")
 


os.system("rm -rf *.mp3")


def bruh(name):
    
    os.system("instantmusic -q -s "+name)
    

@register(outgoing=True, pattern="^.spotify(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("the song is downloading please wait...")
    async with bot.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              await bot.send_message(chat, link)
              respond = await response
          except YouBlockedUserError:
              await event.reply("please unblock @deezloadbot and try again")
              return
          await event.delete()
          await bot.forward_messages(event.chat_id, respond.message)
