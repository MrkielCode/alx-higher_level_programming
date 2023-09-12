"""
functions to convert json value to python values

"""

import json


def from_json_string(my_str):
    my_data = json.loads(my_str)
    return my_data
