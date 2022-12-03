#!/usr/bin/python3
res = ""
for idx in range(97, 123):
    if idx == 101 or idx == 113:
        continue
    res = res + chr(idx)
print("{}".format(res), end="")
