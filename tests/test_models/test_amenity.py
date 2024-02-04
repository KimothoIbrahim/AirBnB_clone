#!/usr/bin/python3

import unittest
from models.amenity import Amenity

am = Amenity()

class TestAmenity(unittest.TestCase):
    """ Test amenities """

    def test_amenity(self):
        """ test for string """
        self.assertTrue(type(am.name), str)

if __name__ == '__main__':
    unittest.main()
