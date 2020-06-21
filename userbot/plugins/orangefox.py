import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register
                
@register(outgoing=True, pattern="^.ofox(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    codename = event.pattern_match.group(1)
    chat = "@ofoxr_bot"
    await event.edit("processing...")
    async with bot.conversation("@ofoxr_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1111224224))
              await conv.send_message(f'/{codename}')
              response = await response
          except YouBlockedUserError:
              await event.reply("please unblock @ofoxr_bot to continue.")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
"xiaomi":
"For Xiaomeme devices only!\
\n\n`.firmware` (codename)\
     \nUsage : Get lastest Firmware\
\n\n`.pb` (codename)\
     \nUsage : Get latest PBRP\
\n\n`.spec` (codename)\
     \nUsage : Get quick spec information about device\
\n\n`.fastboot` (codename)\
     \nUsage : Get latest fastboot MIUI\
\n\n`.recovery` (codename)\
     \nUsage : Get latest recovery MIUI\
\n\n`.of` (codename)\
     \nUsage : Get latest ORangeFox Recovery"})
