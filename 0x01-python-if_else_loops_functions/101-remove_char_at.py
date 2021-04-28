#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    rm = ""

    for count in range(len(str)):
        if count != n:
            rm = rm + str[count]
        count = count + 1
    return rm
