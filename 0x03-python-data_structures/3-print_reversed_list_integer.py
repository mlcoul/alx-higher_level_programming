def print_reversed_list_integer(my_list=[]):

    idx = len(my_list)

    for i in range(idx -1, -1, -1):
        print("{:d}".format(my_list[i]))
