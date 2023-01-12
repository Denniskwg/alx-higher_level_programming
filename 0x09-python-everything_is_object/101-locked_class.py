#!/usr/bin/python3

"""101-locked_class defines a class LockedClass that prevents
the user from dynamically creating new instance attributes
except if the new instance attribute is called first_name

"""


class LockedClass:
    """Locked class with only one attribute first_name"""
    __slots__ = ["first_name"]
