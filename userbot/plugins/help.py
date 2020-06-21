from telethon import events
from datetime import datetime


@command(pattern="^.help")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("⚒ (17) plugins available

    🎨 fun (3) :   dumpster   spam   wtf

    ⚙️ misc (5) :   aria   gdrive   purge   zombies   json 

    💎 plugins (1) :   help

    🧰 tools (6) :   alive   ping power_tools   exec   eval   instant_install_ext_module

    🗂 utils (2) :   speedtest   translate

📕 usage:  .help [plugin_name]")