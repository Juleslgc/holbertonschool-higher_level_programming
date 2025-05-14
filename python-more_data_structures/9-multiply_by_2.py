#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {}
    for keys in a_dictionary:
        new[keys] = a_dictionary[keys] * 2
    return new
