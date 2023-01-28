#!/usr/bin/python3
"""
Square Class: defines a square by : (based on 2-square.py)
"""


class Square:
        """ class Square that defines a square """
        def __init__(self, size=0):
            if type(size) is not int:
                raise TypeError('size must be an integer')
            if (size < 0):
                raise ValueError('size must be >= 0')
            self.__size = size

         def area(self):
             """ Return the area of the square"""
             return (self.__size * self.__size)
