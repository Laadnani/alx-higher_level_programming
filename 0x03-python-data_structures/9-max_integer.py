#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        sorted_list = sorted(my_list)
        return sorted_list[-1]
