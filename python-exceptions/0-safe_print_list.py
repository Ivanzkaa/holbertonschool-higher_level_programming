#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for other_nums in range(x):
        try:
            print("{}".format(my_list[other_nums]), end="")
            number += 1
        except IndexError:
            break
    print()
    return number
