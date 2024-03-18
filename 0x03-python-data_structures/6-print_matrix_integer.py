#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for r in matrix:
        for x in range(len(r)):
            print("{:d}".format(r[x]), end = " ")
