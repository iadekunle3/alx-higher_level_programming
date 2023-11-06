#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{0}".format(num), end=" ")
        print()
