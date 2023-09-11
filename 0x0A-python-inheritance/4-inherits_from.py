#!/usr/bin/python3
"""
This function checked the instance of
a class is a direct inherit
"""


def inherits_from(obj, a_class):
    """
    return true it inherited directly
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
