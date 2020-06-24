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


@register(outgoing=True, pattern="^.deezer(?: |$)(.*)")
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("i need a link to download the song!")
    else:
        await Deezlod.edit("the song is downloading please wait...")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
          try:
              msg_start = await conv.send_message("/start")
              response = await conv.get_response()
              r = await conv.get_response()
              msg = await conv.send_message(d_link)
              otherthings = await conv.get_response()
              song = await conv.get_response()
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await Deezlod.edit("please unblock @deezloadbot and try again")
              return
          await Deezlod.delete()
          await bot.send_file(Deezlod.chat_id, song)
          await Deezlod.client.delete_messages(conv.chat_id,
                                             [msg_start.id, response.id, r.id, msg.id, song.id])
