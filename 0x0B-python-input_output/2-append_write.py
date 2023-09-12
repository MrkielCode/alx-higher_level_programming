#!/usr/bin/python3
"""
This function append text to exixting file
"""


def append_write(filename="", text=""):
    """ function to append a text to file """

    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
