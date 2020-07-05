from telethon import events
from datetime import datetime


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
        global chat_id
        chat_id = event.chat_id
        await event.edit(f"{chat_id}")