#!/usr/bin/python3

"""12-pascal_triangle

"""


def pascal_triangle(n):
    """returns a list of lists representing the Pascal’s
    triangle of n
    """
    my_list = []
    if n <= 0:
        return (my_list)

    for i in range(n):
        list_2 = [1]
        if i > 0:
            if len(my_list[i - 1]) == 1:
                list_2.append(1)
            else:
                for index, item in enumerate(my_list[i - 1]):
                    idx = index + 1
                    if idx < len(my_list[i - 1]):
                        list_2.append(item + my_list[i - 1][idx])
                list_2.append(1)
        my_list.append(list_2)
    return (my_list)
