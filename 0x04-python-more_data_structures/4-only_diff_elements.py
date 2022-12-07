#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = list(set_1 - set_2) + list(set_2 - set_1)
    return set(new_list)
