"""Emoji

Available Commands:

.wtf"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    if input_str == "wtf":
        animation_chars = [
            "w",
            "wh",
            "wha",
            "what",
            "what t",
            "what th",
            "what the",
            "what the f",
            "what the fu",
            "what the fuc",
            "what the fuck"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %11 ])
