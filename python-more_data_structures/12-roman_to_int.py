#!/usr/bin/python3
def roman_to_int(roman_string):

    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string is None or type(roman_string) != str:
        return 0

    add = 0

    for i in range(0, len(roman_string)):
        if i > 0 and rom_num[roman_string[i]] > rom_num[roman_string[i - 1]]:
            add += rom_num[roman_string[i]] - rom_num[roman_string[i - 1]] * 2
        else:
            add += rom_num[roman_string[i]]
    return add
