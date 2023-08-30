#!/usr/bin/python3

""" defining a class square """


class Square:
    """
    A class represent  sqaure with size

    Attributes:
        size (int): size of the square
        position (tuple): represent position of the square

    Methods:
        area(): area of the sqaure
        position(): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):

        """ initialization of size and position
        Args:
            size(int): size of int
            position: size of cordination positon
        """

        self.size = size
        self.position = position

    @property
    def size(self):

        """ getter of size  of square"""

        return (self.__size)

    @size.setter
    def size(self, value):

        """ setter of size of sqaure """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):

        """ getter of sqaure position """

        return (self.__position)

    @position.setter
    def position(self, value):

        """ setter sqaure value """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive")

        self.__position = value

    def area(self):

        """ get the area of square """

        return (self.__size * self.__size)

    def my_print(self):

        """ print the sqaure visualization """

        if self.__size == 0:
            print("")
            return
        """
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        """
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
