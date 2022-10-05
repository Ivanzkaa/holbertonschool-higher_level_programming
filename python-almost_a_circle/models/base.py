#!/usr/bin/python3
"""
Before creating the base class
"""


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
