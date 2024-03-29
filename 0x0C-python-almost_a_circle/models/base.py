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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string
            json_string: json string representation of an
            object
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already
        set
            dictionary: dictionary of attributes to set in
            new instance
        """
        if cls.__name__ == "Rectangle":
            r1 = cls(1, 1)
            cls.update(r1, **dictionary)
            return r1
        if cls.__name__ == "Square":
            s1 = cls(1)
            cls.update(s1, **dictionary)
            return s1

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a json file"""
        instance_list = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                _list = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        else:
            for el in _list:
                instance_list.append(cls.create(**el))
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves instance properties to a csv file in
        csv format
            list_objs: list of instance references
        """
        matrix = []
        rect = ["id", "width", "height", "x", "y"]
        square = ["id", "size", "x", "y"]
        for item in list_objs:
            list_ = []
            item_dict = item.to_dictionary()
            if cls.__name__ == "Rectangle":
                for i in range(len(rect)):
                    list_.append(str(item_dict[rect[i]]))
                matrix.append(list_)
            else:
                for i in range(len(square)):
                    list_.append(str(item_dict[square[i]]))
                matrix.append(list_)

        with open("{}.csv".format(cls.__name__), "w") as f:
            for line in matrix:
                f.write(",".join(line) + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """loads and creates instances from a csv file with
        instance properties
        """
        try:
            with open("{}.csv".format(cls.__name__), "r") as f:
                list_ = []
                rect = ["id", "width", "height", "x", "y"]
                square = ["id", "size", "x", "y"]
                for line in f:
                    list_vals = list(map(int, line.split(",")))
                    if cls.__name__ == "Rectangle":
                        my_dict = {k: v for (k, v) in zip(rect, list_vals)}
                        list_.append(cls.create(**my_dict))
                    else:
                        my_dict = {k: v for (k, v) in zip(square, list_vals)}
                        list_.append(cls.create(**my_dict))
        except FileNotFoundError:
            return []
        else:
            return list_
