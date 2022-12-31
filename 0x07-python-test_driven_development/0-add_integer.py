#!/usr/bin/python3

"""This is the "add_integer" module

function add_integer takes two integers and returns the sum

"""
def add_integer(a, b=98):
    """Returns the sum of a and b
    if either a or b are floats they are cast to int
    """
    try:
        if type(a) != int and type(a) != float:
            raise TypeError("a must be an integer")
        elif type(a) == float:
            a = int(a)
        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        elif type(b) == float:
            b = int(b)
    except Exception as e:
        print(e)
    else:
        return a + b
