#!/usr/bin/python3
"""
before the square class
"""


class Square:
    """
    Initializing the square class
    """
    def __init__(self, size=0):
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

    def my_print(self):
        """
        printing the stdout with the char #
        """
        if self.__size == 0:
            print()
            return None

        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
