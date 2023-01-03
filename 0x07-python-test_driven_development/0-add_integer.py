#!/usr/bin/python3

"""This is the "add_integer" module

function add_integer takes two integers and returns the sum

"""
def add_integer(a, b=98):
    """Returns the sum of a and b
    if either a or b are floats they are cast to int
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(b) == float:
        b = int(b)
    return a + b
