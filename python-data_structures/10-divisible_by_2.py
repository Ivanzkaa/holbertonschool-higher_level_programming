#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for mul_nums in my_list:
        if mul_nums % 2 is 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
