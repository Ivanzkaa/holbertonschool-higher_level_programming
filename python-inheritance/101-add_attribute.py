#!/usr/bin/python3
"""
"""


def add_attribute(obj, key, value):
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("cant' add new attribute")
    setattr(obj, key, value)
