#!/usr/bin/python3
""" This module accepts two arguments which
    are matrix and a integer and return a list
"""


def matrix_divided(matrix, div):

    """ modules to handle matric division

        Args:
        matrix (list): a list of numbers
        div (int): the divisor

        Return: a list of number
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(num, (int, float))
                for num in [elem for row in matrix for elem in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result_matrix
