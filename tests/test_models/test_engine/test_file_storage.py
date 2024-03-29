import unittest
import os
from models import FileStorage
from models.base_model import BaseModel
"""This module defines tests for FileStorage class."""


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class."""

    def setUp(self):
        """Set up method."""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Set up tearDown method."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method."""
        base = BaseModel()
        base.save()
        self.assertIsNotNone(self.storage.all())

    def test_save_new(self):
        """Test save method."""
        base = BaseModel()
        base.save()
        try:
            data = None
            with open("file.json", "r") as f:
                data = f.readlines()
            self.assertIsNotNone(data)
        except Exception as e:
            print(e)

    def test_reload(self):
        """Test reload method."""
        base = BaseModel()
        base.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        data = self.storage.all()[base.__class__.__name__ + "." + base.id]
        self.assertIsNotNone(data)

    def test_file_path(self):
        """Test file_path"""
        base = BaseModel()
        base.save()
        self.storage.reload()
        self.assertTrue(os.path.exists("file.json"))

    def test_objects(self):
        """Test objects"""
        base = BaseModel()
        base.save()
        self.assertIsNotNone(self.storage.all())
