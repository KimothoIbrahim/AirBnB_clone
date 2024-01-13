#!/usr/bin/python3
"""Test for base_model class"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_update(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        first = print(my_model)
        my_model.save()
        second = print(my_model)
        self.assertEqual(first, second)

    def test_dict_to_json(self):
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key, type(my_model_json[key]), my_model_json[key]))
