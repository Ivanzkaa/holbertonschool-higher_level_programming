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
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value
