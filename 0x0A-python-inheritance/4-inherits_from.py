#!/usr/bin/python3

""" Module "4-inherits_from" defines a function inherits_from
that returns True if the passed object is an instance of a
subclass of the specified class else returns False.

"""


def inherits_from(obj, a_class):
    """Returns true if obj is instance of a subclass of a_class"""
    if type(obj) == a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
