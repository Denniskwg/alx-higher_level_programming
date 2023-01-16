#!/usr/bin/python3
"""rectangle module defines a class Rectangle with private
instance attributes width, height, x, y and methods area,
display

"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        for i in [width, height, x, y]:
            validate_int(i)
        for j in [width, height]:
            validate_width_and_height(j)
        for k in [x, y]:
            validate_x_and_y(k)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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
        validate_int(value)
        validate_width_and_height(value)
        self.__width = value

    @height.setter
    def height(self, value):
        validate_int(value)
        validate_width_and_height(value)
        self.__height = value

    @x.setter
    def x(self, value):
        validate_int(value)
        validate_x_and_y(value)
        self.__x = value

    @y.setter
    def y(self, value):
        validate_int(value)
        validate_x_and_y(value)
        self.__y = value

    @classmethod
    def validate_int(attribute):
        if type(attribute) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    @classmethod
    def validate_width_and_height(attribute):
        if attribute <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    @classmethod
    def validate_x_and_y(attribute):
        if attribute < 0:
            raise ValueError("{} must be >= 0".format(attribute))
