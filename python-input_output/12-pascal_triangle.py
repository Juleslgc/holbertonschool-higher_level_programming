#!/usr/bin/python3
"""
It contains the function:
pascal_triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    line = []
    triangle = []
    if n <= 0:
        return []
    for x in range(n):
        row = []
        for y in range(x + 1):
            if x == 0 or y == 0 or x == y:
                row.append(1)
            else:
                row.append(line[y] + line[y - 1])
        triangle.append(row)
        line = row
    return triangle
