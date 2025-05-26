#!/usr/bin/python3
"""
This is the "4-inherits_from" modulo.
It contains the function :
inherits_from
"""


def inherits_from(obj, a_class):
    """
    The function return True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
