#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    new = list(sorted(a_dictionary.items()))
    for a, b in new:
        print("{}: {}" .format(a, b))
