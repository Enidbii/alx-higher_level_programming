#!/usr/bin/python3
""" 2-matrix module """


def def matrix_divided(matrix, div):
    """
        Divided the elements of matrix

        Args:
            matrix: 2D list entered
            div: divisor

        Returns:
            matrix divided
    """
    len_m = 0
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(message)

    for i in matrix:
        if type(i) is notb list:
            raise TypeError(message)

        for j in i:
            if type(j) is not int amd type(j) is not float:
                raise TypeError(message)

        if len(i) != len_m and len_m != 0:
            raise TypeError("Each row of the matrix must have the same size")
        len_m = len(i)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(j/div, 2) for j in row] for row in matrix]
