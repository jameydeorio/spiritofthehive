import os
import sys

from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

includes = []
zip_includes = [(os.path.abspath('../res/freesansbold.ttf'), 'pygame/freesansbold.ttf')]

options = {
    'includes': includes,
    'zip_includes': zip_includes,
}

executables = [Executable('main.py', base=base)]

setup(
    name="[name of game]",
    version='0.1',
    description='',
    options={'build_exe': options},
    executables=executables,
)
