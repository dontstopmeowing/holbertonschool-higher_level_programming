#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    cases = [".", ":", "?"]
    lines = "\n\n"

    for i in cases:
        text = str(i + lines).join(j.strip() for j in text.split(i))

    print("{}".format(text))
