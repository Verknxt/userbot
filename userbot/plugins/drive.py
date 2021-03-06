import asyncio
import os
import time
import math
from datetime import datetime
from telethon import events
from uniborg.util import admin_cmd, progress
from userbot.utils import admin_cmd
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.errors import ResumableUploadError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import file, client, tools
from mimetypes import guess_type
import httplib2


G_DRIVE_TOKEN_FILE = Var.TEMP_DOWNLOAD_DIRECTORY + "/auth_token.txt"
CLIENT_ID = Var.G_DRIVE_CLIENT_ID
CLIENT_SECRET = Var.G_DRIVE_CLIENT_SECRET
OAUTH_SCOPE = "https://www.googleapis.com/auth/drive.file"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
parent_id = Var.GDRIVE_FOLDER_ID
G_DRIVE_DIR_MIME_TYPE = "application/vnd.google-apps.folder"

@borg.on(admin_cmd("drive ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    mone = await event.edit("processing...")
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await mone.edit("this module requires credentials from https://da.gd/so63O aborting!")
        return False
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    required_file_name = None
    if event.reply_to_msg_id and not input_str:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            await mone.edit("downloading to local...")
            downloaded_file_name = await bot.download_media(
                reply_message,
                Var.TEMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return False
        else:
            required_file_name = downloaded_file_name
            await mone.edit("uploading to gdrive...")
    elif input_str:
        input_str = input_str.strip()
        if os.path.exists(input_str):
            required_file_name = input_str
        else:
            await mone.edit("file not found in local server give me a file path")
            return False
    if required_file_name:
        try:
            with open(G_DRIVE_TOKEN_FILE) as f:
                pass
        except IOError:
            storage = await create_token_file(G_DRIVE_TOKEN_FILE, event)
            http = authorize(G_DRIVE_TOKEN_FILE, storage)
            f = open(G_DRIVE_TOKEN_FILE, "r")
            token_file_data = f.read()
            await event.client.send_message(int(Var.PRIVATE_GROUP_ID), "please add var `AUTH_TOKEN_DATA` with the following value:\n\n`" + token_file_data + "`")
        http = authorize(G_DRIVE_TOKEN_FILE, None)
        file_name, mime_type = file_ops(required_file_name)
        try:
            g_drive_link = await upload_file(http, required_file_name, file_name, mime_type,mone,parent_id)
            await mone.edit("uploaded successfully\n\n📄 [{}]({})".format(file_name,g_drive_link))
        except Exception as e:
            await mone.edit(f"exception occurred while uploading to gdrive `{e}`")
    else:
        await mone.edit("file not found in local server give me a file path")

#@command(pattern="^.drivesch ?(.*)")
async def sch(event):
    if event.fwd_from:
        return
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit("this module requires credentials from https://da.gd/so63O aborting!")
        return False    
    try:
        with open(G_DRIVE_TOKEN_FILE) as f:
            pass
    except IOError:
        storage = await create_token_file(G_DRIVE_TOKEN_FILE, event)
        http = authorize(G_DRIVE_TOKEN_FILE, storage)
        f = open(G_DRIVE_TOKEN_FILE, "r")
        token_file_data = f.read()
        await event.client.send_message(int(Var.PRIVATE_GROUP_ID), "please add var `AUTH_TOKEN_DATA` with the following value:\n\n`" + token_file_data + "`")
    http = authorize(G_DRIVE_TOKEN_FILE, None)    
    input_str = event.pattern_match.group(1).strip()
    await event.edit("searching for `{}` in gdrive.".format(input_str))
    if parent_id is not None:
        query = "'{}' in parents and (title contains '{}')".format(parent_id, input_str)
    else:
        query = "title contains '{}'".format(input_str)
    query = "'{}' in parents and (title contains '{}')".format(parent_id,input_str)
    msg = await gsearch(http,query,input_str)
    await event.edit(str(msg))


async def gsearch(http,query,filename):
    drive_service = build("drive", "v2", http=http)
    page_token = None
    msg = "gdrive search query\n`"+filename+"`\nresults\n"
    while True:
        response = drive_service.files().list(q=query,
                                          spaces='drive',
                                          fields='nextPageToken, items(id, title, mimeType)',
                                          pageToken=page_token).execute()
        for file in response.get('items',[]):
            if file.get('mimeType') == "application/vnd.google-apps.folder":
                msg +="`[{}](https://drive.google.com/drive/folders/{}) (folder)`".format(file.get('title'),file.get('id'))+"\n"
            else:
                msg += "`[{}](https://drive.google.com/uc?id={}&export=download)`".format(file.get('title'),file.get('id'))+"\n"
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    return msg        


#@command(pattern="^.gdrivedir ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if CLIENT_ID is None or CLIENT_SECRET is None:
        await event.edit("this module requires credentials from https://da.gd/so63O aborting!")
        return
    if Var.PRIVATE_GROUP_ID is None:
        await event.edit("please set the required environment variable `PRIVATE_GROUP_ID` for this plugin to work")
        return
    input_str = event.pattern_match.group(1)
    if os.path.isdir(input_str):
        if Var.AUTH_TOKEN_DATA is not None:
            with open(G_DRIVE_TOKEN_FILE, "w") as t_file:
                t_file.write(Var.AUTH_TOKEN_DATA)
        storage = None
        if not os.path.isfile(G_DRIVE_TOKEN_FILE):
            storage = await create_token_file(G_DRIVE_TOKEN_FILE, event)
        http = authorize(G_DRIVE_TOKEN_FILE, storage)
        f = open(G_DRIVE_TOKEN_FILE, "r")
        token_file_data = f.read()
        await event.client.send_message(int(Var.PRIVATE_GROUP_ID), "please add var `AUTH_TOKEN_DATA` with the following value:\n\n`" + token_file_data + "`")
        await event.edit("uploading `{}` to gdrive...".format(input_str))
        dir_id = await create_directory(http, os.path.basename(os.path.abspath(input_str)), parent_id)
        await DoTeskWithDir(http, input_str, event, dir_id)
        dir_link = "https://drive.google.com/folderview?id={}".format(dir_id)
        await event.edit(f"successfully uploaded folder to gdrive:\n[{input_str}]({dir_link})")
    else:
        await event.edit(f"directory `{input_str}` does not seem to exist")

async def create_directory(http, directory_name, parent_id):
    drive_service = build("drive", "v2", http=http, cache_discovery=False)
    permissions = {
        "role": "reader",
        "type": "anyone",
        "value": None,
        "withLink": True
    }
    file_metadata = {
        "title": directory_name,
        "mimeType": G_DRIVE_DIR_MIME_TYPE
    }
    if parent_id is not None:
        file_metadata["parents"] = [{"id": parent_id}]
    file = drive_service.files().insert(body=file_metadata).execute()
    file_id = file.get("id")
    drive_service.permissions().insert(fileId=file_id, body=permissions).execute()
    logger.info("created gdrive folder:\nname: {}\nid: {} ".format(file.get("title"), file_id))
    return file_id


async def DoTeskWithDir(http, input_directory, event, parent_id):
    list_dirs = os.listdir(input_directory)
    if len(list_dirs) == 0:
        return parent_id
    r_p_id = None
    for a_c_f_name in list_dirs:
        current_file_name = os.path.join(input_directory, a_c_f_name)
        if os.path.isdir(current_file_name):
            current_dir_id = await create_directory(http, a_c_f_name, parent_id)
            r_p_id = await DoTeskWithDir(http, current_file_name, event, current_dir_id)
        else:
            file_name, mime_type = file_ops(current_file_name)
            g_drive_link = await upload_file(http, current_file_name, file_name, mime_type, event, parent_id)
            r_p_id = parent_id
    return r_p_id


def file_ops(file_path):
    mime_type = guess_type(file_path)[0]
    mime_type = mime_type if mime_type else "text/plain"
    file_name = file_path.split("/")[-1]
    return file_name, mime_type


async def create_token_file(token_file, event):
    flow = OAuth2WebServerFlow(
        CLIENT_ID,
        CLIENT_SECRET,
        OAUTH_SCOPE,
        redirect_uri=REDIRECT_URI
    )
    authorize_url = flow.step1_get_authorize_url()
    async with bot.conversation(int(Var.PRIVATE_GROUP_ID)) as conv:
        await conv.send_message(f"go to the following link in your browser: {authorize_url} and reply the code")
        response = conv.wait_event(events.NewMessage(
            outgoing=True,
            chats=int(Var.PRIVATE_GROUP_ID)
        ))
        response = await response
        code = response.message.message.strip()
        credentials = flow.step2_exchange(code)
        storage = Storage(token_file)
        storage.put(credentials)
        return storage


def authorize(token_file, storage):
    if storage is None:
        storage = Storage(token_file)
    credentials = storage.get()
    http = httplib2.Http()
    credentials.refresh(http)
    http = credentials.authorize(http)
    return http


async def upload_file(http, file_path, file_name, mime_type, event, parent_id):
    drive_service = build("drive", "v2", http=http, cache_discovery=False)
    media_body = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    body = {
        "title": file_name,
        "description": "uploaded using userbot",
        "mimeType": mime_type,
    }
    if parent_id is not None:
        body["parents"] = [{"id": parent_id}]
    permissions = {
        "role": "reader",
        "type": "anyone",
        "value": None,
        "withLink": True
    }
    file = drive_service.files().insert(body=body, media_body=media_body)
    response = None
    display_message = ""
    while response is None:
        status, response = file.next_chunk()
        await asyncio.sleep(1)
        if status:
            percentage = int(status.progress() * 100)
            progress_str = "uploading to gdrive..."
            current_message = "uploading to gdrive..."
            if display_message != current_message:
                try:
                    await event.edit(current_message)
                    display_message = current_message
                except Exception as e:
                    logger.info(str(e))
                    pass
    file_id = response.get("id")
    drive_service.permissions().insert(fileId=file_id, body=permissions).execute()
    file = drive_service.files().get(fileId=file_id).execute()
    download_url = file.get("webContentLink")
    return download_url
