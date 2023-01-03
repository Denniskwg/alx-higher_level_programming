#!/usr/bin/python3
"""3-rectangle

This module defines a class Rectangle that defines a rectangle class.
"""


class Rectangle:
    """Rectangle class with width, height attributes and methods
    area, perimeter, print, and str.
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """Returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = '\n'.join("#" * self.__width \
for j in range(self.__height))
            return result

    @property
    def width(self):
        """Returns current width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): value to set self.__width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns current height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            value (int): value to set self.__width
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
