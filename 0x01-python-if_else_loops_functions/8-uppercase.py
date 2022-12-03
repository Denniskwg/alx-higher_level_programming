#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        c = ord(i)
        if c in range(97, 123):
            c = c - 32
            new = new + chr(c)
        else:
            new = new + chr(c)
    print("{}".format(new))
