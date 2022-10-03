#!/usr/bin/python3
"""
Before creating the class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        the student function in which it's described\
        by it's attributes, it also retrieves a dict\
        representation like json
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        other_dict = {}
        for i in attrs:
            if i in self.__dict__:
                other_dict[i] = self.__dict__[i]
        return other_dict
