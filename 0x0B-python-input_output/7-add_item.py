#!/usr/bin/python3

""" This functions loads a file if not found
it create a new one
"""

from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    This functions load a file or
    create one if not found
    """

    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)

    except FileNotFoundError:
        my_list = []

    for i in range(1, len(argv)):
        my_list.append(argv[i])

    save_to_json_file(my_list, filename)


add_item()
