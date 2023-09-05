#!/usr/bin/python3
"""
module take two arguments and
perfoem addition on them

"""


def add_integer(a, b=98):

    """ Function to add two numbers
    Args:
        a (int): first num to be added
        b (int): second num to be added
    Returns:
        The value of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    num1 = int(a)
    num2 = int(b)

    return (num1 + num2)
