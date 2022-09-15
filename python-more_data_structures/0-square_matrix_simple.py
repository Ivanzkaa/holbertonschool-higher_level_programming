#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for mx in matrix:
        new_matrix.append(list(map(lambda mx: mx ** 2, mx)))
    return new_matrix
