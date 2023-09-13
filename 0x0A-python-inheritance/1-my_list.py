#!/usr/bin/python3

"""
This class inherit list from inbulit class
"""


class MyList(list):

    """
     This class to inherit list class

    """

    def print_sorted(self):

        sorted_list = sorted(self)

        print(sorted_list)
