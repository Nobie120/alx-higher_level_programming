#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for sub_matrix in matrix:
        if len(submatrix) == 0:
            print()
        for num in range(len(sub_matrix)):
            print(
                    "{:d}".format(sub_matrix[i]),
                    end="\n" if i is len(submatrix) - 1 else " ")
