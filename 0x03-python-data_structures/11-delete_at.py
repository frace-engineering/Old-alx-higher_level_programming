#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for x in range(len(my_list)):
        for idx in x:
            my_list[idx] = ''
        return my_list
