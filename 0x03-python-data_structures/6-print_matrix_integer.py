#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, i in enumerate(row):
            print("{:d}".format(i), end=" " if idx != len(row) - 1 else "")
        print()
