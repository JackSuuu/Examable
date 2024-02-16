import os
import platform
import subprocess

# This module is aim to open the file directly when run the program


def pop_out_file(file_path):
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', file_path))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(file_path)
    else:  # linux variants
        subprocess.call(('xdg-open', file_path))


# file = "/Users/jack/Desktop/Learning_Python.pdf"
#
# pop_out_file(file)

