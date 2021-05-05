#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    tmp = my_list[:]
    leng = len(tmp)

    if 0 <= idx < leng:
        tmp[idx] = element
        return (tmp)
    else:
        return (my_list)
