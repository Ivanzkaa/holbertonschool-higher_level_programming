#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for result in enumerate(a_dictionary):
        count += 1
    return count
    print(number_keys(a_dictionary))
