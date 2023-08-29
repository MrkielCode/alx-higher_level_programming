#!/usr/bin/python3

""" This script that perform an exception on sqaure Method """


class Square:

    """
    The class square contains a initialization called size and
    run exception on it
    """

    def __init__(self, size=0):

        """
        Args:
            size: size of a sqaure

            """

        if type(size) is int:

            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
