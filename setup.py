from cx_Freeze import setup, Executable
import sys
build_exe_options = {"packages": ["os", "tkinter"],"excludes": [],}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'include_files': [
        ],
    }
}

executables = [
    Executable(
        'main.py',
        base=base,
        icon='./logo.ico'
    )
]
setup(  name = "MD5文件校验器",
        version = "1.0",
        description = "快速对比两个文件的MD5! ————by.yanhy",
        options=options,
        executables=executables)
