#!/usr/bin/python3

"""1-write_file module defines a function write_file that
writes a text file and returns the number of characters
written

"""


def write_file(filename="", text=""):
    """returns the number of characters written to filename passed"""
    with open(filename, "w") as f:
        return (f.write(text))
