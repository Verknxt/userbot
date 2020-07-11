from telethon import events, errors, functions, types
import inspect
import traceback
import asyncio
import sys
import io
from uniborg.util import admin_cmd


@borg.on(admin_cmd("python"))
async def _(event):
    if event.fwd_from or event.via_bot_id:
        return
    await event.edit("processing...")
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    python = ""
    if exc:
        python = exc
    elif stderr:
        python = stderr
    elif stdout:
        python = stdout
    else:
        python = "success"

    final_output = "python: \n`{}` \n\noutput: \n`{}`".format(cmd, python)

    if len(final_output) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "python.txt"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await event.edit(final_output)


async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)
