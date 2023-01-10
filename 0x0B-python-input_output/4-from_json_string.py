#!/usr/bin/python3

"""4-from_json_t0_string module defines a function from_json_string
that returns an object represented by a JSON string.

"""
import json


def from_json_string(my_str):
    """returns the object representation of JSON string passed"""
    return (json.loads(my_str))
