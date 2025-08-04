import os


def folder_name(path:str):
    return os.path.dirname(path)

def file_name(path:str):
    return os.path.basename(path)

def file_is(path:str):
    return os.path.isfile(path)