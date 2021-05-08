#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}

    for key, i in a_dictionary.items():
        result[key] = i * 2

    return(result)
