#!/usr/bin/python3
"""
This function convert json values to
python values and save it to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function to covert json file and save it
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
