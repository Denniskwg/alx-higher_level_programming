#!/usr/bin/python3
"""6-peak defines a function find peak that finds
a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds the peak of a list of unsorted integers
    Args:
        list_of_integers -  a list of unsorted integers
    returns the peak point of a list
    """
    sums = 0
    peak = 0
    i = 0
    index = 0
    flag = 0
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    while i < len(list_of_integers) - 1:
        if list_of_integers[i] >= list_of_integers[i + 1]:
            if peak < list_of_integers[i]:
                peak = list_of_integers[i]
            if list_of_integers[i] == list_of_integers[i + 1]:
                flag = 1
                return peak
        else:
            addition = list_of_integers[i] + list_of_integers[i + 1]
            if flag == 1:
                index = list_of_integers.index(peak)
            else:
                index = i + 1
            if addition > sums:
                sums = addition
        i = i + 1
    return list_of_integers[index]
