#!/usr/bin/python3
"""
This modules loops through char and
print them also indent it when .?: is
encounter

"""


def text_indentation(text):

    """
    funtions to print strings
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_string = ""
    symbols = ".?:"

    for char in text:
        new_string += char
        if char in symbols:
            new_string = new_string.strip()
            print(new_string, end="\n\n")
            new_string = ""

    if new_string:
        print(new_string.strip(), end="")
