#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_m = []
    for i in matrix:
        new_m.append([list(map(lambda x: x ** 2, i))])
    return new_m
