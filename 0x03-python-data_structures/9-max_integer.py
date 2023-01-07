#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for x in range(len(my_list)):
        if my_list[x] > my_list[x + 1]:
            return my_list[x]
        else:
            return my_list[x +1]
