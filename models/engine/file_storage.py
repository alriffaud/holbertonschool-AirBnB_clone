#!/usr/bin/python3
"""
This module defines FileStorage as a class.
"""
from models.base_model import BaseModel
import json
from datetime import datetime
from os import path


class FileStorage:
    """
    This is a class that serializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        id: is a public instance attribute.
        __file_path: is a string - path to the JSON file.
        __objects: is a dictionary - empty but will store all objects by
        <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This method returns the dictionary __objects.
        """
        return (self.__objects)

    def new(self, obj):
        """
        This method sets in __objects the obj with key <obj class name>.id.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file (path: __file_path).
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        """
        This method deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists.
        """
        class_mapping = {'BaseModel': BaseModel}
        if path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                obj = json.load(f)
                for key, value in obj.items():
                    class_name = value["__class__"]
                    self.new(class_mapping[class_name](**value))
