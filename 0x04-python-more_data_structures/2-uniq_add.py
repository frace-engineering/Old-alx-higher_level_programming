#!/usr/bin/python3
def uniq_add(my_list=[]):
    this_sum = 0
    while (i < len(my_list)):
        for x in my_list:
            if my_list.count(x) == 1:
                this_sum += x
        i++
    this_sum += x
    return (this_sum)
