#!/usr/bin/python3
"""
defining a class
"""


class LockedClass:

    """
    class to check instance of Lockedclass

    """

    __slots__ = ('first_name', )

    def __init__(self):
        self.first_name = None

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute "
            "'{}'".format(name))
        super().__setattr__(name, value)
