# https://pythonflood.com/python-os-module-operating-system-orchestra-5a02973f40af

import os
import pathlib
import subprocess
import argparse
import sys
import shutil
import glob
from pathlib import Path


# home_dir = Path.home()
# print(home_dir)

# home_dir = Path.home()
# print(home_dir)

# home_dir = Path.home()
# print(home_dir)

# cwd = Path.cwd()
# print(cwd)


# curr_file = Path(__file__)
# print(curr_file)

# one_above = Path.cwd().parents[0]
# print(one_above)
# #print(dir(os))

# joined_path = cwd / "output"
# print(joined_path)

# joined_path.mkdir(exist_ok=True)
# print(dir(sys))
# print(os.getcwd())

# print(sys.platform.startswith('linux'))
# subprocess.CompletedProcess
# os.environ.get('TEMP')
# subprocess.call('touch code.py', shell= True)

# subprocess.SubprocessError

# for py in glob.glob("*.py"):
#    print(py)

# print(os.listdir('python-practices'))

# #https://medium.com/@hakanmazi123/python-sys-module-all-notes-6fd57f3adf31


# print(sys.version_info)


# if __name__ == "__main__":
#    pass


import os
import datetime
import glob


# Get all .txt files modified within the last 7 days
files = [
    f
    for f in glob.glob("*.txt")
    if datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(f))
    < datetime.timedelta(days=7)
]
print(files)


import glob


# Match both .txt and .py files
files = glob.glob("*.{txt,py}")
print(files)


from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Print the script's path
print(f"Script path: {script_path}")

# Get the directory of the current script
script_dir = script_path.parent

# Print the script's directory
print(f"Script directory: {script_dir}")

# Example of accessing a file in the same directory
data_file = script_dir / "data.txt"

# Print the path to the data file
print(f"Data file path: {data_file}")
