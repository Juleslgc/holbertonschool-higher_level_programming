#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ord_keys = sorted(a_dictionary)
    for keys in ord_keys:
        print("{}: {}".format(keys, a_dictionary[keys]))
