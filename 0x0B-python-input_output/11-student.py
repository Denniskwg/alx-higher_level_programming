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

    def to_json(self, attrs=None):
        if type(attrs) == list and all(type(item) == str for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        self.first_name = json.get('first_name')
        self.last_name = json.get('last_name')
        self.age = json.get('age')
