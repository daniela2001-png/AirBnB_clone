#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes
this class will be the father class
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    the class BaseModel
    """
    date = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """
        constructor of my class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        parsedValue = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        parsedValue = value
                    setattr(self, key, parsedValue)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        method string of my main class
        """
        return("[{:}] ({:}) {:}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                parsedValue = value.strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                parsedValue = value
            my_dict[key] = parsedValue
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
