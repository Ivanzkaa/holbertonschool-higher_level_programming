#!/usr/bin/python3
def roman_to_int(roman_string):

    rom_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string is None or type(roman_string) != str:
        return 0

    adding_nums = 0

    for nums in range(0, len(roman_string)):
        if nums > 0 and rom_nums[roman_string[nums]] > rom_nums[roman_string[nums - 1]]:
            adding_nums += rom_nums[roman_string[nums]] - rom_nums[roman_string[nums - 1]] * 2
        else:
            adding_nums += rom_nums[roman_string[nums]]
    return adding_nums
