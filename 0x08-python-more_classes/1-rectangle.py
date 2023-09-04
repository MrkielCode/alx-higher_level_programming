#!/usr/bin/python3
"""
Defining a class named Rectangle
that has width and height as an
attributes
"""


class Rectangle:
    """
    This class represent a Rectangle

    Args:
        width(int): the width of the rectangle
        height(int): the height ofthe rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initialize a Rectangle objects

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        To get the width of rectangle

        Return:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            values(int): the value to be set to the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the heigth of the rectangle

        Return:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        To set height of the rectangle
        Args:
            value(int): value to be set to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
