#!/usr/bin/python3

"""5-save_to_json_file module defines a function 5-save_to_json_file
that writes an Object to a text file, using a JSON representation.

"""
import json


def save_to_json_file(my_obj, filename):
    """writes the JSON representation of object passed"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
