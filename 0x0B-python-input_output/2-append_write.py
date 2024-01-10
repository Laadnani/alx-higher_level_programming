#!/usr/bin/pyrhon3
"""def of the entire mod"""

def append_write(filename="", text=""):
    """appending filename with utf-8 enc"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
