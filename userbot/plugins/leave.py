"""
.leave
"""
from telethon.tl.functions.channels import LeaveChannelRequest
from userbot.utils import admin_cmd
import time

@borg.on(admin_cmd("leave", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("i will leave this group in 2 seconds")
        time.sleep(2)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('this is not a chat!')
