#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if (my_list[i] == my_list[-1] or i not in range(x - 1)):
                print("{}".format(my_list[i]))
            else:
                print("{}".format(my_list[i]), end='')
        return i
    except IndexError:
        return i
