#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l_arg = len(argv)
    sum = 0
    for other_nums in range(1, l_arg):
        num = int(argv[other_nums])
        sum += num
    print("{}".format(sum))
