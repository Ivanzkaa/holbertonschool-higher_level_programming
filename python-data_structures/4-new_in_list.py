#!/usr/bin/python3
from copy import copy


def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list
