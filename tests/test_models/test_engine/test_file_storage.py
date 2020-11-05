#!/usr/bin/python3
'''testing file_storage module'''

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    '''Class testing File Storage'''

    json_file = "file.json"
    storage = FileStorage()

    def setUp(self):
        '''init tests'''
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        self.assertFalse(os.path.exists(self.json_file))
        self.storage.clear()

    def test_createJSON(self):
        '''Create a json file'''
        my_model = BaseModel()
        self.assertTrue(os.path.exists(self.json_file))

    def test_loadNoJSON(self):
        '''Create a json file'''
        all_objs = self.storage.all()
        self.assertFalse(all_objs)

    def test_(self):
        '''Create a json file'''
        all_objs = self.storage.all()
        self.assertFalse(all_objs)

    def test_loadJSON(self):
        '''load existing JSON'''
        my_model = BaseModel()
        my_model.name = 'Holberton'
        self.storage.save()
        self.storage.clear()
        all_objs = self.storage.all()
        self.assertFalse(all_objs)
        self.storage.reload()
        all_objs = self.storage.all()
        for attr in all_objs.values():
            self.assertEqual(attr.name, "Holberton")

    def test_typeJSONPATH(self):
        '''check storage FilePATH type'''
        # TODO check how to access a private value
        pass

    def test_checkPublicInstanceTypes(self):
        '''check public instance types'''
        my_model = BaseModel()
        self.assertEqual(type(self.storage.all()), dict)

    def test_type_id(self):
        '''check public instance types'''
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)

    def test_type_created_at(self):
        '''check public instance types'''
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.to_dict()['created_at']), str)

    def test_type_updated_at(self):
        '''check public instance types'''
        my_model = BaseModel()
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.to_dict()['updated_at']), str)

    def test_Base_save(self):
        '''use test'''
        my_model = BaseModel()
        prev = my_model.updated_at
        my_model.save()
        self.assertTrue(my_model.updated_at > prev)

##################
# Unuseless test #
##################

    def test_checkformatID(self):
        '''check id format of storage'''
        my_model = BaseModel()
        all_objs = self.storage.all()
        for key, value in all_objs.items():
            self.assertEqual(key.split('.')[0], "BaseModel")
            id = key.split('.')[1]
            self.assertEqual(value.id, id)


if __name__ == "__main__":
    unittest.main()
