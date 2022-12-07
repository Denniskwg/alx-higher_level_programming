#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    length = len(matrix)
    for i in range(length):
        l = matrix[i]
        new_list.append([x*x for x in l])
    return new_list
