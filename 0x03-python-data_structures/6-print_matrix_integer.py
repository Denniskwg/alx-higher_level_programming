#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for i in matrix:
            length = len(i) - 1
            for x in range(length + 1):
                if x == length:
                    print("{:d}".format(i[x]))
                    break
                else:
                    print("{:d} ".format(i[x]), end="")
