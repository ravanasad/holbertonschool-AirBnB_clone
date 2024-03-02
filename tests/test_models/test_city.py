import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

        City.state_id = "CA"
        City.name = "San Francisco"

        ct = City()

        self.assertEqual(ct.state_id, "CA")
        self.assertEqual(ct.name, "San Francisco")

        City.state_id = ""
        City.name = ""

if __name__ == '__main__':
    unittest.main()

