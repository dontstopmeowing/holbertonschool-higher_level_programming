#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        i = chr(i - 32)
    else:
        i = chr(i)
    print("{:s}".format(i), end="")
