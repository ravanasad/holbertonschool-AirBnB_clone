#!/usr/bin/python
"""This module define for a Base"""


from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
