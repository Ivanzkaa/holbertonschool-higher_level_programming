#!/usr/bin/python3
"""
Befroe the rectangle class
"""


class Rectangle:
    """
    defining the rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializing the rectangle class
        """
        self.__height = height
        self.__width = width

    def area(self):
        """
        calculating the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returning the rectangle perimeter
        """
        if self.__height or self.__width == 0:
            return 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value