#!/usr/bin/python3
"""
Before creating the base class
"""


class Base:
    """
    The creation of the base class 
    """
    def __init__(self, id=None):
        """
        after the base class and the id
        """
        self.__nb_objects = 0
        if id != None:
            self.id = id
        else:
            Base.__nb_objects =+ 1
            self.id = Base.__nb_objects
