#!/usr/bin/python3
"""
functions to convert json value to python values

"""

import json


def from_json_string(my_str):
    """
    function to convert to json string
    """

    my_data = json.loads(my_str)
    return my_data
