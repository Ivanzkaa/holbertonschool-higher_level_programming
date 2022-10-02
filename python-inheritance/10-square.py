#!/usr/bin/python3
"""
inheriting from the base geometry tasks
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    The class square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returning the rectangle area
        """
        return self.__size * self.__size
