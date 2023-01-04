#!/usr/bin/python3
"""This is the "2-matrix_divided" module

function matrix_divided takes a matrix(list of lists) and a number 'div' and
divides each number in the lists with div

"""
def matrix_divided(matrix, div):
    """Returns a new matrix where each list member of the matrix
    is divided by div rounded to 2 decimal places
    """
    if type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    length = len(matrix[0])
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for l in matrix:
        if len(l) != length:
            raise TypeError("Each row of the matrix must have \
the same size")

    for l in matrix:
        for i in range(length):
            if type(l[i]) != int and type(l[i]) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for l in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), l)))

    return new_matrix
