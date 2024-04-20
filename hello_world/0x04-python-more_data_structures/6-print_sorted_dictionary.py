#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    if a_dictionary:
        for key in a_dictionary.keys():
            keys.append(key)

            keys.sort()
            for item in keys:
                print("{}: {}".format(item, a_dictionary[item]))
