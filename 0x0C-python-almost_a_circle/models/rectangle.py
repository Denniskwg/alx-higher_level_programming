#!/usr/bin/python3

"""rectangle module defines a class Rectangle with private
instance attributes width, height, x, y and methods area,
display

"""
from models.base import Base


class Rectangle(Base):
    """defines a simple rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        attrs = ["id", "width", "height", "x", "y"]
        i = len(args)
        idx = 0
        while i:
            setattr(self, attrs[idx], args[idx])
            idx += 1
            i -= 1
