"""

Civilization VI (289070)
Skip the launcher.

"""

from protonfixes import util

import os
import subprocess

def main():
    launcher_path = '2KLauncher/LauncherPatcher.exe'
    bin_path = 'Base/Binaries/Win64Steam'
    #new_path = os.path.join(bin_path, 'CivilizationVI.exe')
    new_path = os.path.join(bin_path, 'CivilizationVI_DX12.exe')
    util.replace_command(launcher_path, new_path)
