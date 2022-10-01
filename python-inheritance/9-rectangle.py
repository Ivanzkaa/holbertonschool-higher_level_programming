#!/usr/bin/python3
"""
inheriting from the base geometry tasks
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


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        integer validation
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returning the rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
