#!/usr/bin/python3
"""
This module takes postive arguments as
and print out symbol "#" based
on the number
"""


def print_square(size):
    """
    function to print square

    Args:
        size (int): size of square to be passed

    Return:
        nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for _ in range(size):
        print("#" * size, end="")
        print()
