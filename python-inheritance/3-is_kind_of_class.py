#!/usr/bin/python3
"""
This is the "3-is_kind_of_class" modulo.
It contains the function :
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    The function return True if the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class
    """
    return isinstance(obj, a_class)
