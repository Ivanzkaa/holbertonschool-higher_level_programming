#!/usr/bin/python3
from tkinter import N


def no_c(my_string):
    remove_char = (my_string.translate({ord(char): None for char in "cC"}))
    return remove_char
