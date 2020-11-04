#!/usr/bin/python3
'''test user class'''

import os
import re
import unittest
from models import storage
from models.user import User
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
        my_user.first_name = "betty"
        my_user.first_name = "holberton"
        my_user.email = "air@holberton.com"
        my_user.save()
        my_str = my_user.__str__()
        r = re.compile(r"\[User\] \(.*\) \{.*\}")
        self.assertIsNotNone(r.match(my_str))

##################
# Unusefull Test #
##################

    def test_Subclass(self):
        '''user class inherit from BaseModel'''
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
