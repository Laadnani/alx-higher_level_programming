#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    for a in set_1:
        if a not in set_2:
            new.append(a)
    for b in set_2:
        if b not in set_1:
            new.append(b)
    return new
