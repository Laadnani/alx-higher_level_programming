#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for a in matrix:
        if len(a) == 0:
            print()
    for a in matrix:
        for b in a:
            print("{:d}" .format(b), end="\n" if b != a[-1] else" ")
        print()
