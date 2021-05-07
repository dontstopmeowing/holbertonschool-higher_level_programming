#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    myList = []
    for x in matrix:
        myList.append(list(map(lambda y: y ** 2, x)))
    return myList
