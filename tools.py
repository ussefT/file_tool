import os


def file_name():
    return os.path.dirname()

def folder_name():
    return os.path.basename()

def file_is(path:str):
    return os.path.isfile(path)