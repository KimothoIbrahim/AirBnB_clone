#!/usr/bin/python3
"""Test for base_model class"""

from models.base_model import BaseModel
import unittest

my_model = BaseModel()

class TestBaseModel(unittest.TestCase):
    def test_base_class(self):
        self.assertEqual(type(my_model), BaseModel)

class TestSave(unittest.TestCase):
    def test_update(self):
        my_model.name = "My First Model"
        my_model.my_number = 89
        first = my_model.updated_at
        my_model.save()
        second = my_model.updated_at
        self.assertFalse(first == second)

class TestDictToJson(unittest.TestCase):
    def test_dict_to_json(self):
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key, type(my_model_json[key]), my_model_json[key]))
        self.assertTrue(my_model_json.__class__)
