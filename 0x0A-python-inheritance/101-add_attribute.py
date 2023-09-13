#!/usr/bin/python3
"""

This function add a new attribute to an
object if it is designed to have one

"""


def add_attribute(obj, attr_name, attr_value):
    """
    To function to add a new atrribute

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
