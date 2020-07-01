from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd


@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("restarting run `.ping` to check if i am online")
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@borg.on(admin_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("turning off manually turn me on later!")
    await borg.disconnect()
