#!/usr/bin/python3
'''
Square Class: Define a Square with private instance

'''


class square:
    ''' class square that defines a square '''
    pass


def __init__(self, size=0):
    ''' initalize variables '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError('size must be >= 0')
    self.__size = size
