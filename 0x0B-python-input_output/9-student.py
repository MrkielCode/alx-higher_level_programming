#!/usr/bin/python3
"""
This has list of public attributes that return as
json
"""


class Student:
    """
    method:
        __int__: intialization of attribute
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
