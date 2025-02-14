import os

def delete(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)



