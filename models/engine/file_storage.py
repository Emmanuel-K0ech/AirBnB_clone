#!/usr/bin/python3
"""Module for file storage"""
import json


class FileStorage:
    """
    Serializes instances to JSON format - json.dumps()
    Deserializes JSON file to instances - json.loads()

    Private attributes
        __file_path - path to json file storage
        __objects - empty dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary of objects in the object {}"""
        return self.__objects

    def new(self, obj):
        """Sets an object in __objects with <obj_class>.id as key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects dictionary into
        JSON string format and saves to __file_path.json"""
        obj_dict = {}
        """#coping the __object{} to a temporary dictionary"""
        for key, obj in self.all().items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __object
        If file does not exist no exception should be raised
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place

        class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place
            }

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as json_file:
                obj_dict = json.load(json_file)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**value)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass
