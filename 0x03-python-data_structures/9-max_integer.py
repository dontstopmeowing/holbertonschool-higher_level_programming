#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list:

        tmp = my_list[0]
        for i in my_list:
            if i > tmp:
                tmp = i
        return tmp
    else:
        return None
