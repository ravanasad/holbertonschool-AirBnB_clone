import unittest
from models.state import State
from models.base_model import BaseModel
"""This is the test for the User class"""


class TestState(unittest.TestCase):
    def test_class_attributes(self):
        self.assertEqual(State.name, "")

        State.name = "Alaska"

        state = State()

        self.assertEqual(state.name, "Alaska")

        State.name = ""


if __name__ == '__main__':
    unittest.main()
