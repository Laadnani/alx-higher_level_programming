#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list(dict.fromkeys(my_list))
    res = sum(new)
    return res

