#!/usr/bin/python3
"""0-rectangle

This module defines a class Rectangle that defines a rectangle
"""
class Rectangle:
    """Defines a rectangle"""
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