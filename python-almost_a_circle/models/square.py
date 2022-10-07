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
        return self.width

    @size.setter
    def size(self, value):
        """the size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigning the argument to the attrributes"""
        if args:
            attri = ["id", "size", "x", "y"]
            for i, b in enumerate(args):
                setattr(self, attri[i], b)

        for a, c in kwargs.items():
            if hasattr(self, a):
                setattr(self, a, c)

    def to_dictionary(self):
        """adding the dictionary"""
        return{
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
