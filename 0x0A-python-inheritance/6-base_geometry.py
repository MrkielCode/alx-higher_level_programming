#!/usr/bin/python3
"""
This class raise an error exception when a
area method is called
"""


class BaseGeometry:
    """
    method:
        area - it raise an exception when
            area is called
    """

    def area(self):
        raise Exception("area() is not implemented")
