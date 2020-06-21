import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


@command(outgoing=True, pattern="^.help$")
async def helpcmd(help):
    await help.edit("⚒ (17) plugins available\n"
                     " \n"
                     "    🎨 fun (2) :   spam   wtf\n"
                     " \n"
                     "    ⚙️ misc (6) :   aria   gdrive   purge   zombies   json   afk\n"
                     " \n"
                     "    💎 plugins (1) :   help\n"
                     " \n"
                     "    🧰 tools (6) :   alive   ping   power_tools   exec   eval   instant_install_ext_module\n"
                     " \n"
                     "    🗂 utils (2) :   speedtest   translate\n"
                     " \n"
                     "📕 usage:  .help [plugin_name]")