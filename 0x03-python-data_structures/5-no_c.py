#!/usr/bin/python3
def no_c(my_string):
    for j in my_string:
        if my_string[j] == " ":
            count += 1
    for x in range(len(my_string) - count):
        if (my_string[x] == 'c' or my_string[x] == 'C'):
            my_string = my_string[x:] + my_string[x + 1:]
    return my_string
