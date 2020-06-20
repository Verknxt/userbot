from telethon import events
from datetime import datetime


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("`pong!`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
                     "`pong!`\n`{}`".format(ms))
