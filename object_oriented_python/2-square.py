#!/usr/bin/python3
"""Square module"""


class Square:
    """defines a square class"""


def __init__(self, size=0):
    """validate square attribute
    Args:
        size: size of the square
    raise:
        typeError: if size is not int
        valueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size
