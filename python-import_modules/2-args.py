#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    if length > 2:
        print("{} arguments:".format(length - 1))
        for num_args in range(1, length):
            print("{}: {}".format(num_args, argv[num_args]))
    elif length == 2:
        print("{} argument:\n{}: {}".format(1, 1, argv[1]))
    else:
        print("0 arguments.")
