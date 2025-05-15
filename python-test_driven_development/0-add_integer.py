#!/usr/bin/python3
"""
This is the "0-add_interger" modulo.
It contains the function :
add_interger
"""


def add_integer(a, b=98):
    """
    Add two integers.

    parameter :
    a : first number.
    b : second number.

    return :
    the sum of a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
