#!/usr/bin/python3

"""
class that inherits of BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes
    """
    name = ""
    state_id = ""
