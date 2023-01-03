#!/usr/bin/python3
"""This is the "5-text_indentation" module

function text_indentation prints a string and adds a
new line if it encounters ".", "?" or ":"

"""
def text_indentation(text):
    """prints text to standard output. if text is
    not a string raise a TypeError exception
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for index in range(len(text)):
        if text[index] in (".", "?", ":"):
            print(text[index], end="")
            print("\n")
        elif text[index] == " " and text[index - 1] in (".", "?", ":"):
            continue
        else:
            print(text[index], end="")
