#!/usr/bin/python3
def uppercase(str):
    space = ""
    for if_upper in str:
        if ord(if_upper) >= 97 and ord(if_upper) <= 122:
            space += chr(ord(if_upper) - 32)
        else:
            space += if_upper
    print("{}".format(space))
