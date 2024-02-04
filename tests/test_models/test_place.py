import unittest
from models.place import Place

place = Place()

class TestAmenity(unittest.TestCase):
    """ Test amenities"""

    def test_amenity(self):
        """ test for string """
        self.assertTrue(type(place.name), str)

if __name__ == '__main__':
    unittest.main()
