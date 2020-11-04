#!/usr/bin/python3
'''test user class'''

import os
import re
import unittest
from models import storage
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
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

    def test_format_str(self):
        '''test __str__'''
        my_user = User()
        my_user.save()
        my_str = my_user.__str__()
        r = re.compile(r"\[User\] \(.*\) \{.*\}")
        self.assertIsNotNone(r.match(my_str))

    def test_type_id(self):
        '''test_type_id'''
        my_user = User()
        self.assertEqual(type(my_user.id), str)

    def test_type_created_at(self):
        '''test_type_created_at'''
        my_user = User()
        self.assertEqual(type(my_user.created_at), datetime)

    def test_type_updated_at(self):
        '''test_type_updated_at'''
        my_user = User()
        self.assertEqual(type(my_user.updated_at), datetime)

    def test_type_first_name(self):
        '''test_type_first_name'''
        my_user = User()
        self.assertEqual(type(my_user.first_name), str)

    def test_type_first_name(self):
        '''test_type_first_name'''
        my_user = User()
        self.assertEqual(type(my_user.first_name), str)

    def test_type_last_name(self):
        '''test_type_last_name'''
        my_user = User()
        self.assertEqual(type(my_user.last_name), str)

    def test_type_email(self):
        '''test_type_email'''
        my_user = User()
        self.assertEqual(type(my_user.email), str)

    def test_type_password(self):
        '''test_type_password'''
        my_user = User()
        self.assertEqual(type(my_user.password), str)

##################
# Unusefull Test #
##################

    def test_Subclass(self):
        '''user class inherit from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
