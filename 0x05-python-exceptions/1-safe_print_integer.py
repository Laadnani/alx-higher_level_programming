#!/bin/usr/python3
def safe_print_integer(value):
    val = False
    try:
        print("{:d}".format(value))
        val = True
        return val
    except:
        return val
