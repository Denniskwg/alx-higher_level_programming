#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    highest = list(a_dictionary.values())[0]
    name = ""
    for k, v in a_dictionary.items():
        if v > highest:
            highest = v
            name = k
    return name
       
