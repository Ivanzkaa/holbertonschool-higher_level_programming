#!/usr/bin/python3
"""
Before creating the base class
"""


import json


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

    def to_json_string(list_dictionaries):
        """the json string representation of list_\
        of dictionaies"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        
