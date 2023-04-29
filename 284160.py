"""

BeamNG.drive (284160)
Launch the linux native build.

"""

from protonfixes import util

import os
import subprocess

def main():
    install_path = util.get_game_install_path()
    bin_path = "BinLinux/BeamNG.drive.x64"
    process = subprocess.Popen(os.path.join(install_path, bin_path))
    process.wait()

    # Don't launch windows version
    os._exit(0)
