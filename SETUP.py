import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": [tkinter]}

base = none
if sys.platform == "win32":
   base = "Win32GUI"

setup(  name = "guifoo",
        version "0.1",
        description "my GUI apllication!",
        options = {"build_exe": build_exe_options},
        executables = [Executables("guifoo.py", base=base)])
