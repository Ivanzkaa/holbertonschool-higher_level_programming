#!/usr/bin/python3
"""
Before doing the function in which\
the rectangle class is created
"""


from models.base import Base


class Rectangle(Base):
    """
    The creation of the rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The function in which we set the property\
        call the fucntion and assign the right\
        attributes for the width, height, y and x.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        the getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        the getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """
        the getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        the setter for y
        """
        if not isinstance(value, int):
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """
        the getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        the setter for x
        """
        if not isinstance(value, int):
            raise ValueError("x must be >= 0")
        self.__x = value
