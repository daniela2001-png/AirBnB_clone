#!/usr/bin/python3
'''test models'''
import unittest
import re
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
        datetime_format = re.compile("\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}..*")
        my_model = BaseModel()
        # test type(created_at)
        self.assertEqual(type(my_model.created_at), datetime)
        # test datetieme_format
        # fromat_found = (datetime_format.match(
        # my_model.to_dict()['created_at']))
        # self.assertIsNotNone(format_found)
        # test value created_at
        self.assertEqual(my_model.created_at.replace(microsecond=0), now)
        # test value changed_no_update
        my_model.save()
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
        # Time skip
        sleep(1)
        # test value changed_no_update
        my_model.save()
        now = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), now)

    def test_str(self):
        '''check __str__ method'''
        my_model = BaseModel()
        r = re.compile("\[BaseModel\] (.*) {.*}")
        my_str = my_model.__str__()
        self.assertIsNotNone(r.match(my_str))
