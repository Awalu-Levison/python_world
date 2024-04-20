#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    if my_list:
        for i in my_list:
            unique_set.add(i)
        return sum(unique_set)

