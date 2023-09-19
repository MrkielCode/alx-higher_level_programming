#!/usr/bin/python3

"""
it inherite the properties of
Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Attributes:
        __size = size of square
        __x: x cordinate of square
        __y: y cordinater of square
        __id = id of the class

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of attributes

        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getting the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ setting the width and height to value """
        self.width = value
        self.height = value

    def __str__(self):
        """ overriding the str method """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ updating the attributes of square """
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.size = value
                elif key == 2:
                    self.x = value
                elif key == 3:
                    self.y = value
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y
                }
