#!/usr/bin/python3
"""
before the class
"""


def text_indentation(text):
    """
    initializing the class to print the function
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_string = "".join([word if word not in ".?:"
                        else word + "\n\n" for word in text])
    print("\n".join([l.strip() for l in new_string.split("\n")]), end="")
