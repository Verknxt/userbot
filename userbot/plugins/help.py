import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


@command(outgoing=True, pattern="^.help$")
async def helpcmd(help):
    await help.edit("⚒ (`17`) plugins available\n"
                     " \n"
                     "    🎨 fun (`2`) :   `spam`   `wtf`\n"
                     " \n"
                     "    ⚙️ misc (`6`) :   `aria`   `gdrive`   `purge`   `zombies`   `json`   `afk`\n"
                     " \n"
                     "    💎 plugins (`1`) :   `help`\n"
                     " \n"
                     "    🧰 tools (`6`) :   `alive`   `ping`   `power_tools`   `exec`   `eval`   `instant_install_ext_module`\n"
                     " \n"
                     "    🗂 utils (`2`) :   `speedtest`   `translate`\n"
                     " \n"
                     "📕 usage:  `.help [plugin_name]`")

@command(outgoing=True, pattern="^.help spam$")
async def helpcmdspam(helpspam):
    await helpspam.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `spam`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.spam`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help wtf$")
async def helpcmdwtf(helpwtf):
    await helpwtf.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `wtf`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.wtf`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help aria$")
async def helpcmdaria(helparia):
    await helparia.edit("⚔️ (`5`) commands available\n"
                     " \n"
                     "🔧 plugin:  `aria`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.amag`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.aurl`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`3`):  `.aclear`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`4`):  `.apause`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`5`):  `.aresume`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help gdrive$")
async def helpcmdgdrive(helpgdrive):
    await helpgdrive.edit("⚔️ (`4`) commands available\n"
                     " \n"
                     "🔧 plugin:  `gdrive`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.gdrive`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.drivesch`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`3`):  `.gdrivedir`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`4`):  `.gfolder`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help purge$")
async def helpcmdpurge(helppurge):
    await helppurge.edit("⚔️ (`5`) commands available\n"
                     " \n"
                     "🔧 plugin:  `purge`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.purge`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.purgeme`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`3`):  `.del`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`4`):  `.edit`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`5`):  `.edit`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help zombies$")
async def helpcmdzombies(helpzombies):
    await helpzombies.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `zombies`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.zombies`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help json$")
async def helpcmdjson(helpjson):
    await helpjson.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `json`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.json`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help help$")
async def helpcmdhelp(helphelp):
    await helphelp.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `help`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.help`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help alive$")
async def helpcmdalive(helpalive):
    await helpalive.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `alive`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.alive`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help ping$")
async def helpcmdping(helpping):
    await helpping.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `ping`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.ping`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help power_tools$")
async def helpcmdpower_tools(helppower_tools):
    await helppower_tools.edit("⚔️ (`2`) commands available\n"
                     " \n"
                     "🔧 plugin:  `power_tools`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.restart`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.shutdown`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help exec$")
async def helpcmdexec(helpexec):
    await helpexec.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `exec`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.exec`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help eval$")
async def helpcmdeval(helpeval):
    await helpeval.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `eval`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.eval`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help instant_install_ext_module$")
async def helpcmdinstant_install_ext_module(helpinstant_install_ext_module):
    await helpinstant_install_ext_module.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `instant_install_ext_module`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.extdl`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help speedtest$")
async def helpcmdspeedtest(helpspeedtest):
    await helpspeedtest.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `speedtest`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.speedtest`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")

@command(outgoing=True, pattern="^.help translate$")
async def helpcmdtranslate(helptranslate):
    await helptranslate.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `translate`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.tr`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "📕 usage:  `.help [command_name]`\n")