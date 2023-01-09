#!/usr/bin/python3

""" Module "5-base_geometry" defines a class BaseGeometry
with an instance method area.

"""


class BaseGeometry(object):
    """class that inherits from object"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")
