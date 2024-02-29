#!/usr/bin/python3
import os
import unittest
from time import sleep

from models.base_model import BaseModel
"""This module defines tests for BaseModel class."""


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class."""

    def tearDown(self):
        """Set up tearDown method."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save_changes_updated_at_when_called(self):
        """Test save method."""
        base = BaseModel()
        time = base.updated_at
        base.save()
        self.assertNotEqual(time, base.updated_at)
    
    def test_to_dict_returns_datetime_as_string_when_called(self):
        """Test to_dict method."""
        base = BaseModel()
        dict = base.to_dict()
        self.assertEqual(str, type(dict['created_at']))

    def test_id_exist_when_object_creating(self):
        """Test id attribute."""
        base = BaseModel()
        self.assertIsNotNone(self.id)

    def test_str_returns_correct_output_when_called(self):
        """Test __str__ method."""
        base = BaseModel()
        expected = f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(base.__str__(), expected)

    def test_save(self):
        """save method"""
        base = BaseModel()
        old = base.updated_at
        sleep(0.1)
        base.save()
        self.assertNotEquals(old, base.updated_at)
