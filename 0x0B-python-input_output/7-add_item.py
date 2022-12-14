#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_List = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_List = []
        save_to_json_file(my_List, "add_item.json")

    n = len(sys.argv)

    if n > 1:
        for i in range(1, n):
            my_List.append(sys.argv[i])

    save_to_json_file(my_List, "add_item.json")
