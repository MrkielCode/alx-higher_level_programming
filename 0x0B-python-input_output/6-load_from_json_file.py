#!/usr/bin/python3

"""
creating a object form file

"""

import json


def load_from_json_file(filename):
    """ creting an object """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
