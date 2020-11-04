#!/usr/bin/python3
'''test user class'''

import os
from models import storage
from unittest import TestCase
from models.user import User
from models.base_model import BaseModel


class TestUser(TestCase):
    '''test class for User class'''

    json_file = "file.json"

    def setUp(self):
        '''init tests'''
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        self.assertFalse(os.path.exists(self.json_file))
        storage.clear()

    def test_demo(self):
        '''test demo'''
        self.assertTrue(True)

    def test_Subclass(self):
        '''user class inherit from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))
