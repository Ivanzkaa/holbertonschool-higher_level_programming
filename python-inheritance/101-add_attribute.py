#!/usr/bin/python3
"""
before creating the function
"""


def add_attribute(obj, key, value):
    """
    adding an attribute
    """
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("cant' add new attribute")
    setattr(obj, key, value)
