import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


@command(outgoing=True, pattern="^.help$")
async def helpcmd(help):
     if not help.text[0].isalpha() and help.text[0] not in ("/", "#", "@", "!"):
        await help.edit("⚒ (`15`) plugins available\n"
                     " \n"
                     "    🎨 fun (`1`) :   `spam`\n"
                     " \n"
                     "    ⚙️ misc (`5`) :   `aria`   `gdrive`   `purge`   `zombies`   `afk`   `leave`\n"
                     " \n"
                     "    💎 plugins (`1`) :   `help`\n"
                     " \n"
                     "    🧰 tools (`4`) :   `alive`   `ping`   `power_tools`   `exec`\n"
                     " \n"
                     "    🗂 utils (`4`) :   `speedtest`   `translate`    `deezer`    `spotify`\n"
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
                     "    📚 info:  `with this command you can send a message multiple times`\n")

@command(outgoing=True, pattern="^.help aria$")
async def helpcmdaria(helparia):
     if not helparia.text[0].isalpha() and helparia.text[0] not in ("/", "#", "@", "!"):
        await helparia.edit("⚔️ (`5`) commands available\n"
                     " \n"
                     "🔧 plugin:  `aria`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.amag`\n"
                     "    📚 info:  `with this command you can download a file from an url`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.aurl`\n"
                     "    📚 info:  `with this command you can download a file from an url`\n"
                     " \n"
                     "    🤖 cmd(`3`):  `.aclear`\n"
                     "    📚 info:  `with this command you can clean all running downloads`\n"
                     " \n"
                     "    🤖 cmd(`4`):  `.apause`\n"
                     "    📚 info:  `with this command you can stop all running downloads`\n"
                     " \n"
                     "    🤖 cmd(`5`):  `.aresume`\n"
                     "    📚 info:  `with this command you can start all running downloads`\n")

@command(outgoing=True, pattern="^.help gdrive$")
async def helpcmdgdrive(helpgdrive):
     if not helpgdrive.text[0].isalpha() and helpgdrive.text[0] not in ("/", "#", "@", "!"):
        await helpgdrive.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `gdrive`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.gdrive`\n"
                     "    📚 info:  `with this command you can upload files to gdrive`\n")

@command(outgoing=True, pattern="^.help purge$")
async def helpcmdpurge(helppurge):
     if not helppurge.text[0].isalpha() and helppurge.text[0] not in ("/", "#", "@", "!"):
        await helppurge.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `purge`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.purge`\n"
                     "    📚 info:  `with this command you can quickly delete many messages`\n")

@command(outgoing=True, pattern="^.help zombies$")
async def helpcmdzombies(helpzombies):
     if not helpzombies.text[0].isalpha() and helpzombies.text[0] not in ("/", "#", "@", "!"):
        await helpzombies.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `zombies`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.zombies`\n"
                     "    📚 info:  `with this command you can remove deleted accounts from a group`\n")

@command(outgoing=True, pattern="^.help help$")
async def helpcmdhelp(helphelp):
     if not helphelp.text[0].isalpha() and helphelp.text[0] not in ("/", "#", "@", "!"):
        await helphelp.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `help`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.help`\n"
                     "    📚 info:  `with this command you can open the help`")

@command(outgoing=True, pattern="^.help alive$")
async def helpcmdalive(helpalive):
     if not helpalive.text[0].isalpha() and helpalive.text[0] not in ("/", "#", "@", "!"):
        await helpalive.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `alive`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.alive`\n"
                     "    📚 info:  `with this command you can find out if your bot works`\n")

@command(outgoing=True, pattern="^.help ping$")
async def helpcmdping(helpping):
     if not helpping.text[0].isalpha() and helpping.text[0] not in ("/", "#", "@", "!"):
        await helpping.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `ping`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.ping`\n"
                     "    📚 info:  `with this command you can measure the ping`\n")

@command(outgoing=True, pattern="^.help power_tools$")
async def helpcmdpower_tools(helppower_tools):
     if not helppower_tools.text[0].isalpha() and helppower_tools.text[0] not in ("/", "#", "@", "!"):
        await helppower_tools.edit("⚔️ (`2`) commands available\n"
                     " \n"
                     "🔧 plugin:  `power_tools`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.restart`\n"
                     "    📚 info:  `with this command you can restart your bot`\n"
                     " \n"
                     "    🤖 cmd(`2`):  `.shutdown`\n"
                     "    📚 info:  `with this command you can shut down your bot`\n")

@command(outgoing=True, pattern="^.help exec$")
async def helpcmdexec(helpexec):
     if not helpexec.text[0].isalpha() and helpexec.text[0] not in ("/", "#", "@", "!"):
        await helpexec.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `exec`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.exec`\n"
                     "    📚 info:  `with this command you can execute python commands`\n")

@command(outgoing=True, pattern="^.help speedtest$")
async def helpcmdspeedtest(helpspeedtest):
     if not helpspeedtest.text[0].isalpha() and helpspeedtest.text[0] not in ("/", "#", "@", "!"):
        await helpspeedtest.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `speedtest`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.speedtest`\n"
                     "    📚 info:  `with this command you can measure the download and upload speed of your bot`\n")

@command(outgoing=True, pattern="^.help translate$")
async def helpcmdtranslate(helptranslate):
     if not helptranslate.text[0].isalpha() and helptranslate.text[0] not in ("/", "#", "@", "!"):
        await helptranslate.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `translate`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.translate`\n"
                     "    📚 info:  `with this command you can translate a message`\n")

@command(outgoing=True, pattern="^.help deezer$")
async def helpcmddeezer(helpdeezer):
     if not helpdeezer.text[0].isalpha() and helpdeezer.text[0] not in ("/", "#", "@", "!"):
        await helpdeezer.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `deezer`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.deezer`\n"
                     "    📚 info:  `with this command you can download a song from deezer`\n")

@command(outgoing=True, pattern="^.help spotify$")
async def helpcmdspotify(helpspotify):
     if not helpspotify.text[0].isalpha() and helpspotify.text[0] not in ("/", "#", "@", "!"):
        await helpspotify.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `spotify`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.spotify`\n"
                     "    📚 info:  `with this command you can download a song from spotify`\n")

@command(outgoing=True, pattern="^.help leave$")
async def helpcmdleave(helpleave):
     if not helpleave.text[0].isalpha() and helpleave.text[0] not in ("/", "#", "@", "!"):
        await helpleave.edit("⚔️ (`1`) command available\n"
                     " \n"
                     "🔧 plugin:  `leave`\n"
                     "📘 about:  `none`\n"
                     " \n"
                     "    🤖 cmd(`1`):  `.leave`\n"
                     "    📚 info:  `with this command you can easily leave a group`\n")
