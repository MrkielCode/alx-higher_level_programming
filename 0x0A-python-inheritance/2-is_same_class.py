#!/usr/bin/python3
"""
This functions checks if the a_class
is an instance of an object
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj - object to be checked
        a_class: parameter to be checked
    """
    if type(obj) is not a_class:
        return False
    return True
