#!/usr/bin/python3
"""
Before writing from the file
"""


def write_file(filename="", text=""):
    """
    writing a string to a text file\
    and returning the number of chars
    """
    with open(filename, "w") as f:
        new_txt = f.write(text)
    return new_txt
