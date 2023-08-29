#!/usr/bin/python3

""" Define a class square """


class Square:

    """
    This class represent a sqaure with a give size

    Attributes:
    __size(int): size of the sqaure

    Methods:
    __init__(self, size= none): size of the square
    """

    def __init__(self, size=0):

        """
        initialize the size of the square

        Args:
            size(int): size of the square

        Raises:
            ValueError: if value is negative
            TypeError: if value is not integer
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculate the area of square

        Returns:
            int: the area of the square
        """
        Area = self.__size * self.__size
        return Area
