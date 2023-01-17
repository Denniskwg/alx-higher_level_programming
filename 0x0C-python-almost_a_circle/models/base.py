#!/usr/bin/python3

"""base module defines a class Base with private
attribute __nb_objects

"""
import json


class Base:
    """simple base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of passed
        object
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs
        to a file
            list_objs: list of onject instances
        """
        json_list = []
        if list_objs is None:
            json_list = cls.to_json_string(json_list)
        else:
            for item in list_objs:
                json_list.append(item.to_dictionary())
            json_list = cls.to_json_string(json_list)
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(json_list)
