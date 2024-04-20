#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for matrix_row in matrix:
        my_matrix.append(list(map(lambda y: y * y, matrix_row)))
    return my_matrix
