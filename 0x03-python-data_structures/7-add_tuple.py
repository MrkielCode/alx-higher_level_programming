#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tup_len_a = len(tuple_a)
    tup_len_b = len(tuple_b)

    if tup_len_a < 2:
        if tup_len_a == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if tup_len_b < 2:
        if tup_len_b == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    result = (sum_first, sum_second)
    return result
