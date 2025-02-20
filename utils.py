import platform
import sys, os
from pathlib import Path
import itertools

project_dir = Path(__name__).resolve().parent

def read_as_binary(filename):
    with open(filename, "rb") as file:
        binary_data = file.read()
    return binary_data

def write_as_binary(filename, data):
    with open(filename, "wb") as file:
        file.write(data)
    return file

def read_as_non_binary(filename):
    with open(filename, "r") as file:
        text_data = file.read()
    return text_data

def write_as_non_binary(filename, data):
    with open(filename, "w") as file:
        file.write(data)
    return file

def get_dir():
    global data
    foldername = 'temp'
    project_dir = Path('.')
    folder_url = project_dir / foldername

    # print("FOLDER_URL: ", folder_url)

    os.makedirs(folder_url, exist_ok=True)
    file_path = folder_url / 'test.txt'

    if os.path.exists(file_path):
        return folder_url
    
    with open(file_path, 'w') as f:
        f.write("Hello, this is a test of Blackout Cry")

    print("Demo file created.")
    return folder_url

def get_os():
    system = platform.system()

    if system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    elif system == "Darwin":
        if "iPhone" in platform.platform() or "iPad" in platform.platform():
            return "iOS"
        return "macOS"
    else:
        return "Unknown OS"

def get_files(dirname='.'):
    files = []
    for entry in os.listdir(dirname):
        file_url = Path(dirname) / entry
        if file_url.is_file():
            files.append(file_url)
        elif file_url.is_dir():
            files.extend(get_files(file_url)) 

    return files