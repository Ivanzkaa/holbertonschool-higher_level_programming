#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[numbers]), end="")
            numbers += 1
        except IndexError:
            numbers += 1
            continue
    print()
    return numbers
