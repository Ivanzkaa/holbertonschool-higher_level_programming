#!/usr/bin/python3
def fizzbuzz():
    for fizz_again in range(1, 101):
        if fizz_again % 3 == 0:
            print("Fizz", end="")
        if fizz_again % 5 == 0:
            print("Buzz", end="")
        if fizz_again % 3 and fizz_again % 5:
            print("{:d}".format(fizz_again), end="")
        print(end=" ")
