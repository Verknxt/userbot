import os
import aria2p
import math
from asyncio import sleep
from subprocess import PIPE, Popen
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register
from userbot.utils import humanbytes, admin_cmd
from requests import get


def subprocess_run(cmd):
    subproc = Popen(cmd, stdout=PIPE, stderr=PIPE,
                    shell=True, universal_newlines=True)
    talk = subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        return
    return talk


trackers_list = get(
    'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt'
).text.replace('\n\n', ',')
trackers = f"[{trackers_list}]"

cmd = f"aria2c \
--enable-rpc \
--rpc-listen-all=false \
--rpc-listen-port 6800 \
--max-connection-per-server=10 \
--rpc-max-request-size=1024M \
--seed-time=0.01 \
--max-upload-limit=5K \
--max-concurrent-downloads=5 \
--min-split-size=10M \
--follow-torrent=mem \
--split=10 \
--bt-tracker={trackers} \
--daemon=true \
--allow-overwrite=true"

subprocess_run(cmd)
if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
download_path = os.getcwd() + TEMP_DOWNLOAD_DIRECTORY.strip('.')

aria2 = aria2p.API(aria2p.Client(host="http://localhost", port=6800,
                                 secret=""))

aria2.set_global_options({'dir': download_path})


@borg.on(admin_cmd("amag(?: |$)(.*)"))
async def magnet_download(event):
    magnet_uri = event.pattern_match.group(1)
    try:
        download = aria2.add_magnet(magnet_uri)
    except Exception as e:
        LOGS.info(str.lower(e))
        return await event.edit("`" + str.lower(e) + "`")
    gid = download.gid
    await check_progress_for_dl(gid=gid, event=event, previous=None)
    await sleep(10)
    new_gid = await check_metadata(gid)
    await check_progress_for_dl(gid=new_gid, event=event, previous=None)


@borg.on(admin_cmd("aurl(?: |$)(.*)"))
async def aurl_download(event):
    uri = [event.pattern_match.group(1)]
    try: 
        download = aria2.add_uris(uri, options=None, position=None)
    except Exception as e:
        LOGS.info(str.lower(e))
        return await event.edit("`{}`".format(str.lower(e)))
    gid = download.gid
    await check_progress_for_dl(gid=gid, event=event, previous=None)
    file = aria2.get_download(gid)
    if file.followed_by_ids:
        new_gid = await check_metadata(gid)
        await check_progress_for_dl(gid=new_gid, event=event, previous=None)

@borg.on(admin_cmd("aclear(?: |$)(.*)"))
async def remove_all(event):
    try:
        removed = aria2.remove_all(force=True)
        aria2.purge_all()
    except Exception:
        pass
    if not removed: 
        subprocess_run("aria2p remove-all")
    await event.edit("clearing on going downloads...")
    await sleep(2.5)
    await event.edit("successfully cleared all on going downloads.")
    await sleep(2.5)


@borg.on(admin_cmd("apause(?: |$)(.*)"))
async def pause_all(event):
    await event.edit("pausing on going downloads...")
    aria2.pause_all(force=True)
    await sleep(2.5)
    await event.edit("successfully paused on going downloads.")
    await sleep(2.5)

@borg.on(admin_cmd("aresume(?: |$)(.*)"))
async def resume_all(event):
    await event.edit("resuming downloads...")
    aria2.resume_all()
    await sleep(1)
    await event.edit("downloads resumed.")
    await sleep(2.5)
    await event.delete()


async def check_metadata(gid):
    file = aria2.get_download(gid)
    new_gid = file.followed_by_ids[0]
    LOGS.info("changing gid " + gid + " to" + new_gid)
    return new_gid


async def check_progress_for_dl(gid, event, previous):
    complete = None
    while not complete:
        file = aria2.get_download(gid)
        complete = file.is_complete
        try:
            if not complete and not file.error_message:
                percentage = int(file.progress)
                downloaded = percentage * int(file.total_length) / 100
                prog_str = "downloading | [`{0}{1}`] `{2}`".format(
                    "".join(["■" for i in range(
                            math.floor(percentage / 10))]),
                    "".join(["▨" for i in range(
                            10 - math.floor(percentage / 10))]),
                    file.progress_string())
                msg = (
                    f"filename: `{file.name}`\n"
                    f"status -> `{file.status.lower()}`\n"
                    f"{prog_str}\n"
                    f"`{humanbytes(downloaded)}` of `{file.total_length_string()}` @ `{file.download_speed_string()}`\n"
                    f"eta -> `{file.eta_string()}`\n"
                )
                if msg != previous:
                    await event.edit(msg)
                    msg = previous
            else:
                await event.edit(f"`{msg}`")
            await sleep(5)
            await check_progress_for_dl(gid, event, previous)
            file = aria2.get_download(gid)
            complete = file.is_complete
            if complete:
                return await event.edit(
                    f"filename: `{file.name}`\n"
                    f"size: `{file.total_length_string()}`\n"
                    f"path: `{TEMP_DOWNLOAD_DIRECTORY + file.name}`\n"
                    "response: `ok - successfully downloaded`"
                )
        except Exception as e:
            if " not found" in str(e) or "'file'" in str(e):
                await event.edit("download canceled:\n`{}`".format(file.name))
                await sleep(2.5)
                return await event.delete()
            elif " depth exceeded" in str(e):
                file.remove(force=True)
                await event.edit(
                    "download auto canceled:\n`{}`\nyour torrent/link is dead."
                    .format(file.name))
