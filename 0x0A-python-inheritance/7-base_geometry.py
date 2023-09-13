#!/usr/bin/python3
"""
This class represent a geometry class

"""


class BaseGeometry:
    """
    method:
        area - it raise an exception when
            area is called

        integer_validator - validate if value is
        an integer
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
