#!/usr/bin/python3
"""writing file with 2 args"""

def write_file(filename="", text=""):
    """reads a filename with utf-8 encoding"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
