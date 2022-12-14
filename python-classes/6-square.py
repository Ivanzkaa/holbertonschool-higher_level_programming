#!/usr/bin/python3
"""
before the square class
"""


class Square:
    """
    the square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing the square class with the position and the size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        setting the position property
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        calulating the size of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        printing the stdout with the char # and position
        """
        if self.__size == 0:
            print()
            return None
        for i in range(self.__position[1]):
            print()
        for a in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
