#!/usr/bin/python3
"""This is the "3-say_my_name" module

function say_my_name takes two strings and prints
a formatted name string

"""
def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    """
    try:
        if type(first_name) != str:
            raise TypeError("first_name must be a string")
        if type(last_name) != str:
            raise TypeError("last_name must be a string")
    except Exception as e:
        print(e)
    else:
        print("My name is {} {}".format(first_name, last_name))
