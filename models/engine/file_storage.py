import json
from models.base_model import BaseModel

"""This module define for a FileStorage class"""


class FileStorage:
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Return all objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        exists ; otherwise, do nothing)"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
        except NameError:
            pass
