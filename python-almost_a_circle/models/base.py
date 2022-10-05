#!/usr/bin/python3
"""
"""


class Base:
    """
    """
    def __init__(self, id=None):
        """
        """
        self.__nb_objects = 0
        if id != None:
            self.id = id
        else:
            Base.__nb_objects =+ 1
            self.id = Base.__nb_objects
