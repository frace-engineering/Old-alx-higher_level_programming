#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        tuple_a = (0, 0)
    elif (len(tuple_a) == 1):
        tuple_a = (tuple_a[0], 0)
    a1, a2 = tuple_a
    if (len(tuple_b) == 0):
        tuple_b = (0, 0)
    elif (len(tuple_b) == 1):
        tuple_b = (tuple_a[0], 0)
    b1, b2 = tuple_b
    ret1 = tuple_a[0] + tuple_b[0]
    ret2 = tuple_a[1] + tuple_b[1]
    new_tuple = (ret1, ret2)
