#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Module "8-rectangle" defines a class Rectangle
that inherits from class BaseGeometry.

"""


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
