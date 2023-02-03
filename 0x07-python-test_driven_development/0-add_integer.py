#!/usr/bin/python3


def add_integer(a, b=98):
    """ Adds two integers """
    if a is not int or float:
        raise TypeError("amust be an integer")
    if b is not int or float:
        raise TypeError("amust be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
