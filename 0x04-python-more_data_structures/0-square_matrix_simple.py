#!/usr/bin/python3
    def square_matrix_simple(matrix=[]):
        quad = lambda z : z ** 2
        new = []
        if  not  matrix:
            return new
        else:
            for i in matrix:
                new.append(list(map(quad, i)))
            return new
