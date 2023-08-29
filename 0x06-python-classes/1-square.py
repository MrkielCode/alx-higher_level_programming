#!/usr/bin/python3
"""
This script creates a class and assign a private attribute
"""


class Square:
    """
    class with an initilization.

    Attributes:
        __size(int): it is  the size of the square

        """
    def __init__(self, size):
        """ initiazing a size of a square

            Args:
                __size: The size of the square

            Return: None
            """
        self.__size = size
