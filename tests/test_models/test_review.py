import unittest
from models.review import Review

rv = Review()

class TestAmenity(unittest.TestCase):
    """ Test amenities"""

    def test_amenity(self):
        """ test for string """
        self.assertTrue(type(rv.text), str)

if __name__ == '__main__':
    unittest.main()
