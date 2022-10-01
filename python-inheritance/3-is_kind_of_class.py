#!/usr/bin/python3
"""
Before the class
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance or if it's an instance\
    of a class that it inherited
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
