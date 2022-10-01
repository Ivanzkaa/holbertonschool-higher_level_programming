#!/usr/bin/python3
"""
Before initializing a class called MyList
"""


class MyList(list):
    """
    the class that will inherit from the list
    """
    def print_sorted(self):
        """
        a function that prints the list in a sorted way
        """
        print(sorted(self))
