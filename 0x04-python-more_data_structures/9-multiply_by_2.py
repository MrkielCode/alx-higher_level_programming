#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dup_list = a_dictionary.copy()
    dup_key = dup_list.keys()
    for i in dup_key:
        dup_list[i] *= 2

    return dup_list
