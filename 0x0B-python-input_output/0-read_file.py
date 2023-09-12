#!/usr/bin/python3
"""
This function take a parameter and
return the file read
"""


def read_file(filename=""):
    """
    args:
    filename: file to be read

    """

    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read())
