import sys
import subprocess
from pathlib import Path
from collections import (
    defaultdict,
    deque,
    OrderedDict,
    ChainMap,
    UserList,
    UserDict,
    UserString,
)


def create_virtual_environment(venv_path):
    try:
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)])
        print(f"Virtual environment created successfully at {venv_path}")
    except Exception as e:
        print(f"Error creating virtual environment: {e}")


if __name__ == "__main__":
    # Get the desired virtual environment path
    venv_name = input("Enter the name for the virtual environment: ")
    venv_path = Path.cwd() / venv_name

    # Check if the virtual environment already exists
    if venv_path.exists():
        print(f"Virtual environment '{venv_name}' already exists. Exiting.")
    else:
        # Create the virtual environment
        create_virtual_environment(venv_path)


# venv\Scripts\activate
# python -m pip install --upgrade pip
# pip freeze > requirements.txt
# pip install -r requirements.txt
