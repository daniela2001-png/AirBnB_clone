#!/usr/bin/python3
'''test models'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


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
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        # test type(created_at)
        self.assertEqual(type(my_model.created_at), datetime)
        # test value created_at
        self.assertEqual(my_model.created_at.replace(microsecond=0), now)
        # test value changed_no_update
        my_model.save
        self.assertEqual(my_model.created_at.replace(microsecond=0), now)

    def test_updated_at(self):
        '''check updated_at'''
        # TODO: created from json
        # TODO: check updated
        now = datetime.now().replace(microsecond=0)
        my_model = BaseModel()
        # test type(created_at)
        self.assertEqual(type(my_model.updated_at), datetime)
        # test value created_at
        self.assertEqual(my_model.updated_at.replace(microsecond=0), now)
        # test value changed_no_update
        print()
        print(my_model.updated_at.replace(microsecond=0))
        sleep(2)
        my_model.save
        print(my_model.updated_at.replace(microsecond=0))
        print(datetime.now())
        print(now)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), now)

    def test_str(self):
        '''check __str__ method'''
        my_model = BaseModel()
        self.assertTrue(my_model.id)
