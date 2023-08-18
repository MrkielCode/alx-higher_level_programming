#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_fig = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }

    total = 0
    pre_val = 0

    for i in roman_string[::-1]:

        val = roman_fig[i]

        if val < pre_val:
            total = total - val
        else:
            total += val
        pre_val = val

    return total
