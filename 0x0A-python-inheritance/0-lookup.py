#!/usr/bin/python3
"""
This function return a list of attributes
associated with a class
"""
def lookup(obj):
    """
    args:
        obj: class object to be checked
    """
    return dir(obj)

