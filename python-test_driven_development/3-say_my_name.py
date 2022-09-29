#!/usr/bin/python3
"""
before the class and the fucntion for the string
"""


def say_my_name(first_name, last_name=""):
    """
    after initializing the class for the function
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))