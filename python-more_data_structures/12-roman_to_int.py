#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string is None or type(roman_string) != str:
        return 0

    adding_nums = 0

    for more_nums in range(0, len(roman_string)):
        if more_nums > 0 and roman_num[roman_string[more_nums]] > roman_num[roman_string[more_nums - 1]]:
            adding_nums += roman_num[roman_string[more_nums]] - roman_num[roman_string[more_nums - 1]] * 2
        else:
            adding_nums += roman_num[roman_string[more_nums]]
    return adding_nums
