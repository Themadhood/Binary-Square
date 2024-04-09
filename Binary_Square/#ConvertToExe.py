#program:       ConvertToExe
#purpose:       is a game
#progamer:      Madison Arndt 10/26/2023

_VERSION = "0.0.0"

import PyInstaller.__main__
import os

_FP = os.path.dirname(__file__)

PyInstaller.__main__.run([f'{_FP}/x18.py',
                          #'--console',
                          '--onefile',
                          '--noconsole',
                          f'--icon={_FP}/THEMADHOOD.ico',
                          f"--add-data={_FP}/THEMADHOOD.ico;.",
                          "--clean"])























