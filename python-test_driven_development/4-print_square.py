#!/usr/bin/python3
"""
This is the "4-print_square" modulo.
It contains the function :
print_square
"""


def print_square(size):
    """"
    Prints a square with the character #

    parameter:
    size : Number of character at print.

    return :
    The number of #.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print('#' * size)
