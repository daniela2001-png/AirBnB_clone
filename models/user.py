#!/usr/bin/python3

"""
class that inherits of BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    define atributtes for this class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
