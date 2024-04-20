#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_tuple = ()
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    temp_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return temp_tuple

"""
In Line4 and Line5 zeros are added
because we maintain the maximum number
of 2 elements in each tuple as per
instructions

"""
