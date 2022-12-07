#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    flag = 0
    for k, v in a_dictionary.items():
        if k == key:
            flag = 1
            break
        else:
            continue
    if flag == 1:
        del a_dictionary[key]
    return a_dictionary
