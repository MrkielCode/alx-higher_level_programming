#!/usr/bin/python3
"""
This function check if class
inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (type) - object to be if inherited from
        a_class (class) - class to be matched
    """
    if not isinstance(obj, a_class):
        return False
    return True
