def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for x in my_list:
        print("{:d}".format(x, end=''))
