#!/usr/bin/python3

""" Module "5-base_geometry" defines a class BaseGeometry
with an instance method area and integer_validator.

"""


class BaseGeometry(object):
    """class that inherits from object"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
