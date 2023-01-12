#!/usr/bin/python3
def uniq_add(my_list=[]):
    this_sum = 0
    for x in set(my_list):
        this_sum += x
    print(this_sum)
