#!/usr/bin/python3
"""
    This modules accepts two arguments as string
    and print them
"""


def say_my_name(first_name, last_name=""):
    """
    The modules handles two arguments and print them

    Args:
        first_name(str): it accept first string
        last_name(str): it accept second strings

    Return:
        it return full name if success

    Raises:
        TypeError: if arguments are numbers
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
