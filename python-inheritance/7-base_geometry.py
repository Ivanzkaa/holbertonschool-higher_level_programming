#!/usr/bin/python3
"""
Before creating an empty class
"""


class BaseGeometry:
    """
    The creation of an empty class called BaseGeometry
    """
    def area(self):
        """
        a public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validating the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
