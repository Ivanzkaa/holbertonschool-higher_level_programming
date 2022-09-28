#!/usr/bin/python3
"""
the class for the square
"""


class Square:
    """
    the class with the square and the private size instance
    """
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
