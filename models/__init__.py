#!/usr/bin/python3

"""
init the a instance of a class Filestorage
and we will reload the class to dict
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
