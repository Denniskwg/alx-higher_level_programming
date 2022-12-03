#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if ord(i) == 99 or ord(i) == 67:
            continue
        new_str += i
    return new_str
