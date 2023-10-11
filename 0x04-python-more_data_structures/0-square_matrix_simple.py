#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda submatrix: map(lambda x: x**2 for x in submatrix)))
