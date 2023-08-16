#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    sum_num = 0
    for i in unique_list:
        sum_num = sum_num + i
    return sum_num
