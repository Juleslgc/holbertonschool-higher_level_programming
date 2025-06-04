#!/usr/bin/python3
"""
It contains the class:
Student
"""


class Student:
    """
    Create class student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__
