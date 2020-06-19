# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.speedtest$")
async def speedtest(spd):
    """ For .speedtest command, use SpeedTest to check server speeds. """
    await spd.edit("`running speedtest...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("`"
                   "download: "
                   f"{speed_convert(result['download'])} \n"
                   "upload: "
                   f"{speed_convert(result['upload'])} \n"
                   "`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'kb/s', 2: 'mb/s', 3: 'gb/s', 4: 'tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

CMD_HELP.update(
    {"ping": "`.ping`\
    \nUsage: Shows how long it takes to ping your bot.\
    \n\n`.speed`\
    \nUsage: Does a speedtest and shows the results."
})
