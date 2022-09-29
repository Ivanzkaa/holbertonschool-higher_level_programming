#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    """
    """
    new_list = []

    for column in range(len(matrix)):
        for row in range(len(matrix[column])):
            if not isinstance(matrix[column][row], (int, float)):
                raise TypeError("matris ust be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("divisio by zero")

    for i in matrix:
        new_list.append(list(map(lambda i: round(i / div, 2), i)))
    return new_list