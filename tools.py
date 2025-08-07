import os


def file_rename(path:str):
    os.rename(path)

def file_search(path:str):
    return path if os.path.exists(path) else 'Not Found'

def folder_create(path:str='out'):
    os.mkdir(path)

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
