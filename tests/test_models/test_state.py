import unittest
from models.state import State

st = State()

class TestAmenity(unittest.TestCase):
    """ Test amenities"""

    def test_amenity(self):
        """ test for string """
        self.assertTrue(type(st.name), str)

if __name__ == '__main__':
    unittest.main()
