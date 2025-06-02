#!/usr/bin/python3
"""
It contains the function:
read_file
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, 'r', encoding="utf-8") as fichier:
        print(fichier.read(), end="")
