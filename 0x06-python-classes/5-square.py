#!/usr/bin/python3

""" Define a class square """


class Square:

    """ This class represent a sqaure with a give size"""

    def __init__(self, size=0):

        """
        initialize the size of the square
        """
        self.size = size

    def area(self):
        """
        Calculate the area of square

        Returns:
        int: the area of the square
        """
        Area = self.__size * self.__size
        return Area

    def my_print(self):
        """ To print # base on size """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """ getter to get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter to get size """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
