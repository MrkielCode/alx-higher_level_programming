#!/usr/bin/python3

"""
    This module multiply two number
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplication of matrix.

    Args:
        m_a (list of lists of ints/floats): The matrix to be multiply
        m_b (list of lists of ints/floats): The matrix to be multiply 
    """

    return (np.matmul(m_a, m_b))
