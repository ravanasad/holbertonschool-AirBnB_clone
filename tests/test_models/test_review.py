import unittest
from models.review import Review
from models.base_model import BaseModel
"""This is the test for the User class"""


class TestReview(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

        Review.place_id = "5"
        Review.user_id = "3"
        Review.text = "text"

        rw = Review()

        self.assertEqual(rw.place_id, "5")
        self.assertEqual(rw.user_id, "3")
        self.assertEqual(rw.text, "text")

        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""


if __name__ == '__main__':
    unittest.main()
