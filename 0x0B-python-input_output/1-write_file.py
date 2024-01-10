#!/usr/bin/python3
"""read_file function that read a file"""

def write_file(filename="", text=""):
    """ reads filename with utf-8 encoding"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
