#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    quad = lambda z : z ** 2
    new = []
    for i in matrix:
        new.append(list(map(quad, i)))
    return new
