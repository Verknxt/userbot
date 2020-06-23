import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


@command(outgoing=True, pattern="^.help$")
async def helpcmd(help):
     if not help.text[0].isalpha() and help.text[0] not in ("/", "#", "@", "!"):
        await help.edit("⚒ (`16`) plugins available\n"
                     " \n"
                     "    🎨 fun (`2`) :   `spam`   `wtf`\n"
                     " \n"
                     "    ⚙️ misc (`6`) :   `aria`   `gdrive`   `purge`   `zombies`   `afk`\n"
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
     if not helpspam.text[0].isalpha() and helpspam.text[0] not in ("/", "#", "@", "!"):
         await helpspam.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `spam`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.spam`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help wtf$")
async def helpcmdwtf(helpwtf):
     if not helpwtf.text[0].isalpha() and helpwtf.text[0] not in ("/", "#", "@", "!"):
        await helpwtf.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `wtf`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.wtf`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help aria$")
async def helpcmdaria(helparia):
     if not helparia.text[0].isalpha() and helparia.text[0] not in ("/", "#", "@", "!"):
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
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help gdrive$")
async def helpcmdgdrive(helpgdrive):
     if not helpgdrive.text[0].isalpha() and helpgdrive.text[0] not in ("/", "#", "@", "!"):
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
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help purge$")
async def helpcmdpurge(helppurge):
     if not helppurge.text[0].isalpha() and helppurge.text[0] not in ("/", "#", "@", "!"):
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
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help zombies$")
async def helpcmdzombies(helpzombies):
     if not helpzombies.text[0].isalpha() and helpzombies.text[0] not in ("/", "#", "@", "!"):
        await helpzombies.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `zombies`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.zombies`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help help$")
async def helpcmdhelp(helphelp):
     if not helphelp.text[0].isalpha() and helphelp.text[0] not in ("/", "#", "@", "!"):
        await helphelp.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `help`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.help`\n"
                     "    📚 info:  `none`")

@command(outgoing=True, pattern="^.help alive$")
async def helpcmdalive(helpalive):
     if not helpalive.text[0].isalpha() and helpalive.text[0] not in ("/", "#", "@", "!"):
        await helpalive.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `alive`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.alive`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help ping$")
async def helpcmdping(helpping):
     if not helpping.text[0].isalpha() and helpping.text[0] not in ("/", "#", "@", "!"):
        await helpping.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `ping`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.ping`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help power_tools$")
async def helpcmdpower_tools(helppower_tools):
     if not helppower_tools.text[0].isalpha() and helppower_tools.text[0] not in ("/", "#", "@", "!"):
        await helppower_tools.edit("⚔️ (`2`) commands available\n"
                     " \n"
                     "🔧 plugin:  `power_tools`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.restart`\n"
                     "    📚 info:  `none`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.shutdown`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help exec$")
async def helpcmdexec(helpexec):
     if not helpexec.text[0].isalpha() and helpexec.text[0] not in ("/", "#", "@", "!"):
        await helpexec.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `exec`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.exec`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help eval$")
async def helpcmdeval(helpeval):
     if not helpeval.text[0].isalpha() and helpeval.text[0] not in ("/", "#", "@", "!"):
        await helpeval.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `eval`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.eval`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help instant_install_ext_module$")
async def helpcmdinstant_install_ext_module(helpinstant_install_ext_module):
     if not helpinstant_install_ext_module.text[0].isalpha() and helpinstant_install_ext_module.text[0] not in ("/", "#", "@", "!"):
        await helpinstant_install_ext_module.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `instant_install_ext_module`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.extdl`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help speedtest$")
async def helpcmdspeedtest(helpspeedtest):
     if not helpspeedtest.text[0].isalpha() and helpspeedtest.text[0] not in ("/", "#", "@", "!"):
        await helpspeedtest.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `speedtest`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.speedtest`\n"
                     "    📚 info:  `none`\n")

@command(outgoing=True, pattern="^.help translate$")
async def helpcmdtranslate(helptranslate):
     if not helptranslate.text[0].isalpha() and helptranslate.text[0] not in ("/", "#", "@", "!"):
        await helptranslate.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `translate`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.tr`\n"
                     "    📚 info:  `none`\n")
