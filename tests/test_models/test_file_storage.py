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
        self.base = BaseModel()
        self.storage.reload()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method."""
        self.base.save()
        self.assertIsNotNone(self.storage.all())
    def test_new(self):
        """Test new method."""
        self.storage.new(self.base)
        self.assertTrue(self.base in self.storage.all().values())

    def test_save(self):
        """Test save method."""
        self.base.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test reload method."""
        self.base.save()
        self.storage.reload()
        self.assertTrue(os.path.exists("file.json"))

    def test_file_path(self):
        """Test file_path method."""
        self.base.save()
        self.storage.reload()
        self.assertTrue(os.path.exists("file.json"))

    def test_objects(self):
        """Test objects method."""
        self.base.save()
        self.assertIsNotNone(self.storage.all())

