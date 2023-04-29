"""

Skyrim Special Edition (489830)
Installs and launches MO2.

"""

from protonfixes import config
from protonfixes import util

import json
import os
import urllib.request

exe_path = os.path.join(util.get_game_install_path(), 'SkyrimSELauncher.exe')
exit_early = False

@util.once
def first_run():
    globals()['exit_early'] = True

@util.once(retry=True)
def install_mo2():
    url = ''

    response = urllib.request.urlopen('https://api.github.com/repos/ModOrganizer2/modorganizer/releases/latest').read()
    response_dict = json.loads(response)

    version = response_dict['tag_name'][1:]
    for asset in response_dict['assets']:
        if version + '.exe' in asset['name']:
            url = asset['browser_download_url']

    if url == '':
        os._exit(-1)

    file_name = os.path.basename(url)
    file_path = os.path.join(config.cache_dir, file_name)
    urllib.request.urlretrieve(url, file_path)

    util.replace_command(exe_path, file_path)

    globals()['exit_early'] = True

def launch_mo2():
    mo2 = os.path.join(util.protonprefix(), 'drive_c/Modding/MO2/ModOrganizer.exe')
    util.replace_command(exe_path, mo2)

def main():
    # Do nothing on first run.
    first_run()

    if exit_early:
        return 0

    # Install MO2 if we have not done so already.
    install_mo2()

    if exit_early:
        return 0

    launch_mo2()
