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

    def test_new(self):
        """Test new method."""
        base = BaseModel()
        self.assertTrue(base in self.storage.all().values())

    def test_save(self):
        """Test save method."""
        base = BaseModel()
        self.assertIsNotNone(self.storage.all())

    def test_reload(self):
        """Test reload method."""
        base = BaseModel()
        base.save()
        self.storage.reload()
        self.assertIsNotNone(self.storage.all())

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
