#!/usr/bin/python3
"""
"""


def pascal_triangle(n):
    """
    """
    the_list = []
    if n <= 0:
        return the_list

    row = [1]
    x = [0]
    for i in range(max,(n, 0)):
        print(row)
        row = [var + other_var for var, other_var in zip(row + x, x + row)]
    return the_list
