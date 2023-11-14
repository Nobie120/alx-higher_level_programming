#!/usr/bin/python3

def natrix_divided(matrix, div):
    """ function that divides all elements of a matrix.

    Args:
        matrix:The matrix
        div:the nuberthat divides elements of the matrix
    Raises:
        TypeError:matrix must be a matrix (list of lists) of integers/floats
        TypeError:div must be a number
    Returns:
        a new matrix
    """

    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError("""matrix must be a matrix
                        (list of lists) of integers/floats""")
    if not isinstance(matrix, list) or \
    not all(isinstance(row, list)for row in matrix) or \
    not all(isinstance(obj, (int, float))for row in matrix for obj in row):
        raise TypeError("""matrix must be a matrix
                        (list of lists) of integers/floats""")
    if all(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return[[round(x / 2) for obj in row]for row in matrix]
