#!/usr/bin/python3
"""
Before the function
"""


import json


def load_from_json_file(filename):
    """
    the function that creates an object\
    from a json file
    """
    with open(filename, "r") as f:
        return json.load(f)
