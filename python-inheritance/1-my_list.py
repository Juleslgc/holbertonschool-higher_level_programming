#!/usr/bin/python3
"""
This is the "1-my_list" modulo.
It contains the class :
MyList
"""


class MyList(list):
    """
    Print sorted list
    """
    def print_sorted(self):
        print(sorted(self))
