#!/usr/bin/python3
def delete_at(my_list[], idx=0):
    for x in range(len(my_list)):
        if (idx < 0 or idx >= len(my_list) - 1):
            return my_list
        elif x == idx:
            del my_list[idx]
    return my_list
