#!/usr/bin/python3
def roman_to_int(roman_string):

    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string is None or type(roman_string) != str:
        return 0

    add_nums = 0

    for nums in range(0, len(roman_string)):
        if nums > 0 and rom_num[roman_string[nums]] > rom_num[roman_string[nums - 1]]:
            add_nums += rom_num[roman_string[nums]] - rom_num[roman_string[nums - 1]] * 2
        else:
            add_nums += rom_num[roman_string[nums]]
    return add_nums
