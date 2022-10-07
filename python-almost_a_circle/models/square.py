#!/usr/bin/python3
"""Before the inheritance from the rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """the creation of the square class and calling the supper innit"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """returning the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """the size getter"""
        return self.size
    @size.setter
    def size(self, value):
        """the size setter"""
        self.width = value
        self.height = value
