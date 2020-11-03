#!/usr/bin/python3

"""
a class FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances
"""

import models
import json
from models.user import User
from datetime import datetime


class FileStorage:
    """
    <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
    <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
    -> <class 'BaseModel'>
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary. """
        return self.__objects

    def new(self, obj):
        """ add a dictionary """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            # aqui el updated y el create son datetimes
            self.__objects[key] = obj

    def save(self):
        """ Serializes to JSON file. """
        new_dict = {}
        for key in self.__objects.keys():  # aqui el created  updated datetime
            new_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        reaload the objects type(dict)
        """
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, mode="r") as fo:
                data = json.load(fo)
                # agregamos el diccionario de dicionarios
                for key, value in data.items():
                    if key.split('.')[0] == 'BaseModel':
                        new = BaseModel(**value)
                    elif key.split('.')[0] == 'User':
                        new = User(**value)
                    self.__objects[key] = new
        except FileNotFoundError:
            pass

    def clear(self):
        '''Clear objectes, this was used for tests'''
        self.__objects = {}
