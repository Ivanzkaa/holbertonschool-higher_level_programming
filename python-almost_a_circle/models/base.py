#!/usr/bin/python3
"""
Before creating the base class
"""


import json
from operator import index
from os import path


class Base:
    """
    The creation of the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
        after the base class and initializing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the json string representation of list_\
        of dictionaies"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writing the json strin representation\
        of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                n_obj = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(n_obj))

    @staticmethod
    def from_json_string(json_string):
        """returning the list of the JSON string\
        representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returning the instance with all attributes\
        already set"""
        if cls.__name__ == "Rectangle":
            dummy_func = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_func = cls(1, 1)
        dummy_func.update(**dictionary)
        return dummy_func

    @classmethod
    def load_from_file(cls):
        """returning the list of the instances"""
        if path.exists(cls.__name__ + "json") is False:
            return []
        with open(cls.__name__ + "json", "r") as file:
            list = cls.from_json_string(file.read())
            return [cls.create(**index) for index in list]
