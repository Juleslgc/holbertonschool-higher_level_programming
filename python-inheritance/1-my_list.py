#!/usr/bin/python3
"""
This is the "1-my_list" modulo.
It contains the class :
MyList
"""


class MyList(list):
    """
    Class mylist
    """
    def print_sorted(self):
        """
        Print sorted list
        """
        print(sorted(self))
