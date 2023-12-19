#!/usr/bin/python3
""" Define a Class """


class Square:
    """Constructor.

    Args:
        size: side size of the square.

    Raise:
        TypeError: if the size is not an int
        ValueError: if size if less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('Size must be >= 0')
    self.__size = size
