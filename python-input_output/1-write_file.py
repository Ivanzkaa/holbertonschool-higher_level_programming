#!/usr/bin/python3
"""
"""


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        new_txt = f.write(text)
    return new_txt
