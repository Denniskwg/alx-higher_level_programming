#!/usr/bin/python3
"""module square definws a class Square

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self._Rectangle__x,
                                                 self._Rectangle__y,
                                                 self._Rectangle__width)

    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        super().validate_int("width", value)
        super().validate_width_and_height("width", value)
        self._Rectangle__width = value
        super().validate_int("width", value)
        super().validate_width_and_height("width", value)
        self._Rectangle__height = value
