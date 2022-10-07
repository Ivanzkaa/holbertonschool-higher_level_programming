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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        the width setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """the height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """the x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """the y getter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """printing the rectangle with the char # """
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for s_char in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        updating the class so that it returns the rectangle id\
        x, y, width and height
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """assigning the argument to the attrributes"""
        if args:
            attri = ["id", "width", "height", "x", "y"]
            for i, b in enumerate(args):
                setattr(self, attri[i], b)
