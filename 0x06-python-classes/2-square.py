#!/usr/bin/python3
'''
Square Class: Define a Square with private instance

'''


class Square:
    ''' class square defines a square '''
    def __init__(self, size=0):
        ''' initalize variables '''
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError('size must be >= 0')
