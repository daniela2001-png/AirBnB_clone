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

    def test_id(self):
        '''check id'''
        my_model = BaseModel()
        self.assertTrue(my_model.id)
        self.assertEqual(type(my_model.id), str)

    def test_created_at(self):
        '''check created_at'''
        # TODO: created from json
        from datetime import datetime
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_updated_at(self):
        '''check updated_at'''
        # TODO: created from json
        # TODO: check updated
        from datetime import datetime
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_str(self):
        '''check __str__ method'''
        my_model = BaseModel()
        self.assertTrue(my_model.id)
