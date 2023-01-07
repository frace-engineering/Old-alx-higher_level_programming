#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == " ":
        return None
    for x in range(len(my_list)):
        if my_list[x] > my_list[x + 1]:
            return my_list[x]
        else:
            return my_list[x +1]
