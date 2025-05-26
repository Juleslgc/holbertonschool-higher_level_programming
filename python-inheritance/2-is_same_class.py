#!/usr/bin/python3
"""
This is the "2-is_same_class" modulo.
It contains the function :
is_same_class
"""


def is_same_class(obj, a_class):
    """
    The function return True if the object
    is exactly an instance of the class.
    """
    return type(obj) is a_class
