#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):

    def test_save_changes_updated_at_when_called(self):
        base = BaseModel()
        time = base.updated_at
        base.save()
        self.assertNotEqual(time, base.updated_at)
    
    def test_to_dict_returns_datetime_as_string_when_called(self):
        base = BaseModel()
        dict = base.to_dict()
        self.assertEqual(str, type(dict['created_at']))

    def test_id_exist_when_object_creating(self):
        base = BaseModel()
        self.assertIsNotNone(self.id)

    def test_str_returns_correct_output_when_called(self):
        base = BaseModel()
        expected = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base.__str__(), expected)