#!/usr/bin/python3
def uppercase(str):
    for if_upper in str:
        if ord(if_upper) >= 97 and ord(if_upper) <= 122:
            if_upper += chr(ord(if_upper) - 32)
            print("{}".format(if_upper))
