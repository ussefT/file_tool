import os


def folder_name(path:str):
    return os.path.dirname(path)

def file_name(path:str):
    return os.path.basename(path)

def file_is(path:str):
    return os.path.isfile(path)

def files_folder(path:str):
    if os.path.isdir(path):
        for file in os.listdir(path):
            yield file
