#!/usr/bin/python3

"""6-load_from_json_file module defines a function 6-load_from_json_file
that creates an Object from a “JSON file”.

"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r") as f:
        return (json.loads(f.readline()))
