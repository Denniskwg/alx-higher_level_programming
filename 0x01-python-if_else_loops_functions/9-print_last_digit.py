#!/usr/bin/python3
def print_last_digit(number):
    if type(number) == int:
        for digit in str(number):
            i = digit
        print("{}".format(i), end="")
        return i
