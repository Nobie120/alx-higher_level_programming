#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix1 = matrix.copy()
    return list(map(lambda sub: list(map(lambda x: x**2, sub)), matrix1))
