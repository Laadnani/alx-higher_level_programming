#!/usr/bin/python3
def no_c(my_string):
    dup = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        dup += i
    return dup
