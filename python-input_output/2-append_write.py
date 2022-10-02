#!/usr/bin/python3
"""
Before writing from the file
"""


def append_write(filename="", text=""):
    """
    writing a string to a text file\
    and returning the number of chars
    """
    with open(filename, "a") as f:
        new_txt = f.write(text)
    return new_txt
