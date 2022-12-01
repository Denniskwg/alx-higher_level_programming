#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    _dir = dir(hidden_4)
    avoid = "__"
    for i in range(0, len(_dir)):
        if avoid not in _dir[i]:
            print("{}".format(_dir[i]))
