#!/usr/bin/python3
"""Define a Class"""

class Square:
    """ Define a squre"""

    def __init__(self, size=0):

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('Size must be >= 0')
    self.__size = size
