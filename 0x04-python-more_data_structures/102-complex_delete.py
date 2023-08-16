#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dup_keys = list(a_dictionary.keys())

    for j in dup_keys:
        if value == a_dictionary.get(j):
            del a_dictionary[j]
    return (a_dictionary)
