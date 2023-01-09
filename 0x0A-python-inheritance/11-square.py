#!/usr/bin/python3

""" Module "11-square" defines a class Square
that inherits from class Rectangle.

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
