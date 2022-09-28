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
        self.__size = size
        self.__position = position

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
        for element in value:
            if element < 0:
                raise TypeError("position must be a tuple of\
                    2 positive integers")
            else:
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
