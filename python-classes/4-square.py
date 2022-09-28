#!/usr/bin/python3
"""
Before the square class
"""


class Square:
    """
    the square class
    """
    def __init__(self, size=0):
        """
        initializing the square
        """
        self.__size = size

    def area(self):
        """
        calculating the size of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
