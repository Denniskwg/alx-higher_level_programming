#!/usr/bin/python3

"""3-to_json_string module defines a function to_json_string
that returns  the JSON representation of an object.

"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of object passed"""
    return (json.dumps(my_obj))
