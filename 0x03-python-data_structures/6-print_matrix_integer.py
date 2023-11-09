#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for w in matrix:
        print(' '.join("{:d}".format(element) for element in w))
