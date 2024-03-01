import unittest
from models.user import User
from models.base_model import BaseModel
"""This is the test for the User class"""


class TestUser(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

        User.email = "default@example.com"
        User.password = "default_password"
        User.first_name = "John"
        User.last_name = "Doe"

        user = User()

        self.assertEqual(user.email, "default@example.com")
        self.assertEqual(user.password, "default_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""


if __name__ == '__main__':
    unittest.main()
