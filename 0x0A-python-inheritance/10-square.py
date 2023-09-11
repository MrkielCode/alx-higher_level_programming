#!/usr/bin/python3

"""
The sqaure class inherit the properties
of the Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    methods:
        __init__: intialize the height the width and
        height
    """
    def __init__(self, size):
        super().__init__(size, size)
