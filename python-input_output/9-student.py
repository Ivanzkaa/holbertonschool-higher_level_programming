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

    def to_json(self):
        return self.__dict__
