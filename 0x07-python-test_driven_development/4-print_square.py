#!/usr/bin/python3
"""This is the "4-print_square" module

function print_square prints a square with # of a
given size

"""
def print_square(size):
    """prints a square of size size. size must be an
    integer
    """
    try:
        if type(size) == float and size < 0:
            raise TypeError("size must be an integer")
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
    except Exception as e:
        print(e)
    else:
        for i in range(size):
            for j in range(size):
                if j == size - 1:
                    print("#")
                else:
                    print("#", end="")
