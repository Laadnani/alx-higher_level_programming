#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tmpo = []
    for i in my_list:
        if i % 2 == 0:
            tmpo.append(True)
        else:
            tmpo.append(False)
    return tmpo
