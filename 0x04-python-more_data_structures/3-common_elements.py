#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for a in set_1:
        if a in set_2 and a in set_1:
           new.append(a)
        else:
            continue
    return new
