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

    with open(filename, "r", encoding="utf-8") as myfile:
        print("{}".format(myfile.read(), end=""))
