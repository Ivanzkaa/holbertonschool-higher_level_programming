#!/usr/bin/python3
"""
inheritence form another class
"""


class MyInt(int):
    """
    the class Myint
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def  __ne__(self, other):
        return super().__eq__(other)
