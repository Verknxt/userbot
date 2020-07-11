import re
from requests import get
from bs4 import BeautifulSoup

from userbot import CMD_HELP
from userbot.utils import register


@borg.on(admin_cmd("magisk$"))
async def magisk(request):
    magisk_dict = {
        "stable":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/stable.json",
        "beta":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/master/beta.json",
        "canary":
        "https://raw.githubusercontent.com/topjohnwu/magisk_files/canary/release.json"
    }
    releases = 'latest magisk releases:\n'
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        releases += f'{name}: [zip {data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                    f'[apk {data["app"]["version"]}]({data["app"]["link"]}) | ' \
                    f'[uninstaller]({data["uninstaller"]["link"]})\n'
    await request.edit(releases)
