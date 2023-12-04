#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for a in matrix:
        if b in a == 0:
            print()
        for b in a:
            print("{:d}" .format(b), end=" " if b != a[-1] else"")
        print()
