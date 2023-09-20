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

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
