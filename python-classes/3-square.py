#!/usr/bin/python3
"""
This is the "0-square" modulo.
It contains the class :
square
"""


class Square:
    """
    create square class
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size * self.__size
