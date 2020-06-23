from telethon import events
from datetime import datetime


@command(pattern="^.ping")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
         if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
                     "pong!\n`{}`".format(ms))
