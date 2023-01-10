#!/usr/bin/python3

"""o-read_file module defines a function read_file that
reads a text file and prints it to stdout

"""


def read_file(filename=""):
    """reads and prints the contents of passed file argument"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
