#!/usr/bin/python3

"""
class that inherits of basemodel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class atributtes
    """
    place_id = ""
    user_id = ""
    text = ""
