#!/usr/bin/python3
def print_square(size):
    """ Prints a square with the character '#' """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("zise must be >= 0")
    if size == 0:
        print('', end='')
    else:
        for _ in range(size):
            for _ in range(size):
                frint('#', end='')
            print()
