import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

        Place.city_id = "5"
        Place.user_id = "3"
        Place.name = "Example Place"
        Place.description = "Example description"
        Place.number_rooms = 2
        Place.number_bathrooms = 1
        Place.max_guest = 4
        Place.price_by_night = 100
        Place.latitude = 123.4
        Place.longitude = -78.9
        Place.amenity_ids = ["wifi", "pool", "parking"]

        plc = Place()

        self.assertEqual(plc.city_id, "5")
        self.assertEqual(plc.user_id, "3")
        self.assertEqual(plc.name, "Example Place")
        self.assertEqual(plc.description, "Example description")
        self.assertEqual(plc.number_rooms, 2)
        self.assertEqual(plc.number_bathrooms, 1)
        self.assertEqual(plc.max_guest, 4)
        self.assertEqual(plc.price_by_night, 100)
        self.assertEqual(plc.latitude, 123.4)
        self.assertEqual(plc.longitude, -78.9)
        self.assertEqual(plc.amenity_ids, ["wifi", "pool", "parking"])

        Place.city_id = ""
        Place.user_id = ""
        Place.name = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

if __name__ == '__main__':
    unittest.main()

