#!/usr/bin/python3
"""Function that divides
    all elements of a matrix"""


def matrix_divided(matrix, div):
    new = []
    mylist = 0
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    for k in matrix:
        if len(k) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        if type(i) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        new.append([])
        for j in i:
            result = round(j / div, 2)
            if type(j) != int and type(j) != float:
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[mylist].append(result)
        mylist += 1
    return (new)
