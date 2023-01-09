#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Module "8-rectangle" defines a class Rectangle
that inherits from class BaseGeometry.

"""


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
