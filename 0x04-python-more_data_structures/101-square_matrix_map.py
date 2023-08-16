#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda j: list(map(lambda k: k**2, j)), matrix)))
