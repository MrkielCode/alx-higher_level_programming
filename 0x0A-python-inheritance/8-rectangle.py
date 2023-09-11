#!/usr/bin/python3
"""
This class represent a geometry class

"""


class BaseGeometry:
    """
    method:
        area - it raise an exception when
            area is called

        integer_validator - validate if value is
        an integer
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


"""
This class represent a rectangle class
"""


class Rectangle(BaseGeometry):

    """
    A rectangle class that inherit from
    the base class

    method:
        __init__: To initialize an attributes
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
    """

    def __init__(self, width, height):
        self.width = width
        self.height = width
        self.integer_validator("width", width)
        self.integer_validator("height", height)
