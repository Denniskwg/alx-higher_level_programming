#!/usr/bin/python3

"""Defines a class Student with method to_json and attributes
first name, last name and age.

"""


class Student:
    """class that defines a student."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
