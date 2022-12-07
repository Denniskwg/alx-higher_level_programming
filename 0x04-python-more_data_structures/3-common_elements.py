#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in set_1:
        for x in set_2:
            if i == x:
                new_list.append(x)
    return set(new_list)
