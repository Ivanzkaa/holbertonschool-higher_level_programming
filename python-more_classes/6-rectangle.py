#!/usr/bin/python3
"""
Before the class
"""


class Rectangle:
    """
    initializing the number of instances
    """
    number_of_instances = 0
    """
    Creating the rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializing the rectangle class
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances -= 1

    def area(self):
        """
        calculating the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returning the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

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

    def __str__(self):
        """
        the new string
        """
        new_strng = ""
        if self.__width == 0 or self.__height == 0:
            return new_strng
        for width in range(self.__height - 1):
            new_strng += ("#" * self.__width) + "\n"
        new_strng += ("#" * self.__width)
        return new_strng

    def __repr__(self):
        """
        the string representation of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        deleting the rectangle, also dealing with the instances
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
