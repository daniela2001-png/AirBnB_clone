#!/usr/bin/python3

"""
class BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    our class BaseModel
    """
    date = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """
        constructor of my class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key is not "__class__":
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

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        my_dict = self.__dict__
        if "created_at" in my_dict:
            if type(my_dict["created_at"]) is not str:
                my_dict["created_at"] = datetime.now().strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                my_dict["created_at"] = self.created_at
        if "updated_at" in my_dict:
            if type(my_dict["updated_at"]) is not str:
                my_dict["updated_at"] = datetime.now().strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                my_dict["updated_at"] = self.updated_at
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
