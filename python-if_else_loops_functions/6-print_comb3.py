#!/usr/bin/python3
for dif_numbers in range(0, 10):
    for other_numbers in range(0, 10):
        if dif_numbers < other_numbers:
            if dif_numbers < 8:
                print("{}{},".format(dif_numbers, other_numbers), end=" ")
            else:
                print("{}{}".format(dif_numbers, other_numbers))
