#!/usr/bin/python3
"""
a class called MyList
"""


class MyList(list):
    def print_sorted(self):
        """
        a function that prints the list in a sorted way
        """
        print(sorted(self))
