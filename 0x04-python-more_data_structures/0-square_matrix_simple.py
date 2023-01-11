#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        arr = list(map(lambda y: y * y, x))
        new_matrix.append(arr)
    return new_matrix
