#!/usr/bin/python3
"""
The rectangle class inherit attributes from
the BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height