#!/usr/bin/python3
"""1-square

This module defines a class "Square" that defines a square
"""


class Square:
    """class Square defines a square by size"""
    def __init__(self, size=0):
        self.__size = size
        if not type(self.__size) == int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returns:
            current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns:
            current size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value (int): value to set self.__size
        """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
