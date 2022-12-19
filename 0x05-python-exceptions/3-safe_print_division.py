#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        return None
    else:
        return res
    finally:
        print("Inside result: {}".format(res))
