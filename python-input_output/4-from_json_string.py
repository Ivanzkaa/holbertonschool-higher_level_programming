#!/usr/bin/python3
"""
before json import and the function
"""


import json


def from_json_string(my_str):
    """
    a function that returns an object\
    represented by json string
    """
    return json.loads(my_str)
