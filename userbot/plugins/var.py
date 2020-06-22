""" Userbot module which contains everything related to \
    downloading/uploading from/to the server. """
import aiohttp
import asyncio
import os
import time
from datetime import datetime
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
import json
import subprocess
import math
from pySmartDL import SmartDL
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.utils import register
from userbot.utils import admin_cmd, humanbytes, progress, time_formatter
from userbot.uniborgConfig import Config
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
import io
from userbot.utils import admin_cmd, progress

@borg.on(admin_cmd(pattern="download(?: |$)(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mone = await event.reply("processing...")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await event.client.download_media(
                reply_message,
                Config.TMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
        else:
            await mone.edit("downloaded to `{}`".format(downloaded_file_name))
    elif input_str:
        url = input_str
        file_name = os.path.basename(url)
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        if "|" in input_str:
            url, file_name = input_str.split("|")
        url = url.strip()
        file_name = file_name.strip()
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
        downloader.start(blocking=False)
        c_time = time.time()
        while not downloader.isFinished():
            total_length = downloader.filesize if downloader.filesize else None
            downloaded = downloader.get_dl_size()
            display_message = ""
            now = time.time()
            diff = now - c_time
            percentage = downloader.get_progress() * 100
            speed = downloader.get_speed()
            elapsed_time = round(diff) * 1000
            progress_str = "{0}{1}\nProgress: {2}%".format(
                ''.join(["█" for i in range(math.floor(percentage / 5))]),
                ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
                round(percentage, 2))
            estimated_total_time = downloader.get_eta(human=True)
            try:
                current_message = f"downloading..."
                if round(diff % 10.00) == 0 and current_message != display_message:
                    await mone.edit(current_message)
                    display_message = current_message
            except Exception as e:
                logger.info(str(e))
        end = datetime.now()
        ms = (end - start).seconds
        if downloader.isSuccessful():
            await mone.edit("downloaded to `{}`".format(downloaded_file_name))
        else:
            await mone.edit("incorrect url\n {}".format(input_str))
    else:
        await mone.edit("reply to a message to download to my local server.")        

@borg.on(admin_cmd(pattern="upload (.*)", outgoing=True))                
async def _(event):
    if event.fwd_from:
        return
    mone = await event.reply("processing...")
    input_str = event.pattern_match.group(1)
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    if os.path.exists(input_str):
        start = datetime.now()
        c_time = time.time()
        await bot.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            supports_streaming=False,
            allow_cache=False,
            reply_to=event.message.id,
            thumb=thumb
        )
        await mone.edit("uploaded successfully")
    else:
        await mone.edit("file not found!")

CMD_HELP.update({
    "download":
    ".download <link|filename> or reply to media\
\nUsage: Downloads file to the server.\
\n\n.upload <path in server>\
\nUsage: Uploads a locally stored file to the chat."
})
