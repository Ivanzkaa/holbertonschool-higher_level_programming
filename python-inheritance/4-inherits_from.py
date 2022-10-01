#!/usr/bin/python3
"""
Before the function that will inherit\
directly or indirectly from a specific class
"""


def inherits_from(obj, a_class):
    """
    a function that will return True if it inherits\
    directly or indirectly from a speficic class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
