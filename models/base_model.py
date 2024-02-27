#!/usr/bin/python
"""This module define for a Base"""


from datetime import datetime
from time import strftime
import uuid


class BaseModel:
    """BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
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

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)