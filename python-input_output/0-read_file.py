#!/usr/bin/python3
"""
a function that will read from a file
"""


def read_file(filename=""):
    """
    reading the text from a file
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
