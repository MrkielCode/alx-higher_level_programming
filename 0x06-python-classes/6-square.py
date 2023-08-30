#!/usr/bin/python3

""" Define a class square """


class Square:

    """ This class represent a sqaure with a give size"""

    def __init__(self, size=0):

        """
        initialize the size of the square
        """
        self.size = size

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square cordinate."""
        self.size = size
        self.position = position

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
            return
        """
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        """
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    @property
    def size(self):
        """ getter to get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter to get size """
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        return self.__position

    @position.setter
    def position(self, value):

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value