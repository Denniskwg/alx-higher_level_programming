#!/usr/bin/python3
"""1-square

This module defines a class "Square" that defines a square
Defaults size to 0. Raise error on invalid size inputs.
Attribute position which takes a default (0, 0) tuple.
Methods Getter and Setter properties for size and position.
Method area returns size of area of the square.
Method my_print prints the square using "#", moved over left and top using
position tuple.
"""


class Square:
    """class Square defines a square by size
    Also defines position using a tuple, which defaults (0, 0).
    Square can also get area, and print square using '#'.
    When printing, using position, offset on top and left.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size
        if not type(self.__size) == int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in self.__position:
                if type(i) is not int or i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if type(i) is not int or i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    if j in range(self.__size - 1):
                        print("#", end='')
                    else:
                        print("#")
