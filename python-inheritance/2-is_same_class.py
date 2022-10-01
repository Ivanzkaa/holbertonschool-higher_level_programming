#!/usr/bin/python3
"""
Before the function
"""


def is_same_class(obj, a_class):
    """
    A fucntion that if it's exactly the same instance return True
    """
    if isinstance(obj, a_class):
        return True
    return False
