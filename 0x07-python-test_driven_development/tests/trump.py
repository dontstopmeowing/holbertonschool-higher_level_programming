#!/usr/bin/python3
import sys

sys.path.append('../')

add_integer = __import__('0-add_integer').add_integer

# Trump: if we didn't test, we'd be fine

print(add_integer(2 * 2, 500))
