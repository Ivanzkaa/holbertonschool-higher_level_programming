#!/usr/bin/python3
def uppercase(str):
    for if_upper in str:
        if ord(97) <= ord(if_upper) <= ord(122):
            if_upper += chr(ord(if_upper) - 32)
            print("{:s}".format(if_upper), end="")
        print("")
