#!/usr/bin/python3
'''test models'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''test BaseModel'''

    def test_createAttr(self):
        '''create Instance'''
        my_model = BaseModel()
        my_model.name = "Holberton"
        self.assertEqual(my_model.name, "Holberton")
