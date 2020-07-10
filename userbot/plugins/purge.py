from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils import register, errors_handler, admin_cmd

@borg.on(admin_cmd("purge$"))
@errors_handler
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat,
                                               min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "purge complete!\npurged `" + str(count) + "` messages.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "purge of `" + str(count) + "` messages done successfully.")
    await sleep(2)
    await done.delete()

@borg.on(admin_cmd("purgeme"))
@errors_handler
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "purge complete!\npurged `" + str(count) + "` messages.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
            "purge of `" + str(count) + "` messages done successfully.")
    await sleep(2)
    i = 1
    await smsg.delete()

@borg.on(admin_cmd("del$"))
@errors_handler
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "deletion of message was successful")
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "well i can't delete a message")

@borg.on(admin_cmd("edit"))
@errors_handler
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "edit query was executed successfully")

@borg.on(admin_cmd("sd"))
@errors_handler
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "sd query done successfully")