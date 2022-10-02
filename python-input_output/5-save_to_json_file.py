#!/usr/bin/python3
"""
before the function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    the function in which it read from the filename\
    and it opens the json file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
