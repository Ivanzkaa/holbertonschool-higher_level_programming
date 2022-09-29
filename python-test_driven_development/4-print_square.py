#!/usr/bin/python3
"""
before the class for the square
"""


def print_square(size):
    """
    function that prints the square with a char
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be <= 0")
    elif isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)