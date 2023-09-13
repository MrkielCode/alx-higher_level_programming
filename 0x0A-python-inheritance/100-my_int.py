#!/usr/bin/python3

"""
This class that inherit int class
and overide thw methods

"""


class MyInt(int):
    """
    Inheriting the int class

    """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
