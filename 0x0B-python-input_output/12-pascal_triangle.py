#!/usr/bin/python3
""" pascal triangle function """


def pascal_triangle(n):
    """
    returns a list of lists of integers
    Args:
        n: lists and integers
    """
    h_line = [[1 for j in range(i + 1)] for i in range(n)]
    for n in range(n):
        for i in range(n - 1):
            h_line[n][i + 1] = sum(h_line[n - 1][i:i + 2])
    return h_line
