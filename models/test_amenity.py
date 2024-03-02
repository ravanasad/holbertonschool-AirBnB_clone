import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(Amenity.name, "")

        Amenity.name = "Example Amenity"

        amenity = Amenity()

        self.assertEqual(amenity.name, "Example Amenity")

        Amenity.name = ""

if __name__ == '__main__':
    unittest.main()
