#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return my_list
        elif x == idx:
            my_list[idx] == element
        return my_list
