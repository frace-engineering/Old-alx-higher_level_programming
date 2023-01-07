#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in range(len(my_list)):
       
        if (((x == idx) < 0) or ((x == idx) > len(my_list))):
            return (my_list)
        else:
            my_list[idx] == element
            return (my_list)
