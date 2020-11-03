#!/usr/bin/python3
'''testing file_storage module'''

from unittest import TestCase
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorage(TestCase):
    '''Class testing File Storage'''

    json_file = "file.json"

    def setUp(self):
        '''init tests'''
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        self.assertFalse(os.path.exists(self.json_file))
        storage.clear()

    def test_helloworld(self):
        '''simple assertTrue'''
        self.assertTrue(True)

    def test_createJSON(self):
        '''Create a json file'''
        my_model = BaseModel()
        self.assertTrue(os.path.exists(self.json_file))

    def test_loadNoJSON(self):
        '''Create a json file'''
        all_objs = storage.all()
        self.assertFalse(all_objs)

    def test_loadJSON(self):
        '''load existing JSON'''
        my_model = BaseModel()
        my_model.name = 'Holberton'
        storage.save()
        storage.clear()
        all_objs = storage.all()
        self.assertFalse(all_objs)
        storage.reload()
        all_objs = storage.all()
        for attr in all_objs.values():
            self.assertEqual(attr.name, "Holberton")

