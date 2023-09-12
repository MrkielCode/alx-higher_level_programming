#!/usr/bin/python3
"""
This function convert python values to
json data
"""

import json


def to_json_string(my_obj):
    """ convert python values to json data """

    my_data = json.dumps(my_obj)
    return my_data
