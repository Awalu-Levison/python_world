#!/usr/bin/python3
"""create a class square"""


class Square:
    """square attributes
    Args:
        __size: the size of the square
    """

    def __init__(self, size):
        """initialise square
        Args:
            size (int): size of the side of a square
        Returns: None
        """
        self.__size = size
