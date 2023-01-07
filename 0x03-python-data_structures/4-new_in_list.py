#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        new_list = my_list
        for x in range(len(new_list)):
            if ((idx < 0) or (idx > len(new_list) - 1)):
                return new_list
            else:
                new_list[idx] = element
                return new_list
