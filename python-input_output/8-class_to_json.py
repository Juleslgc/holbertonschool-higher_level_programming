#!/usr/bin/python3
"""
It contains the functions:
class_to_json
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple
    data structure for JSON serialization of an object.
    """
    return obj.__dict__
