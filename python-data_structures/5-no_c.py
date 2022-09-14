#!/usr/bin/python3
def no_c(my_string):
    remove_char = (my_string.translate({ord(char): None for char in "cC"}))
    return remove_char
