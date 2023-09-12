#!/usr/bin/python3
"""
The function write to a file and return the
length
"""


def write_file(filename="", text=""):
    """ To write and return the length of the file"""

    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.write(text)
    return len(text)
