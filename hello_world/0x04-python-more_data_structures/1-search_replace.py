#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, item in enumerate(new_list):
        if item == search:
            new_list[i] = replace
    return new_list
"""enumerate: Track index of an element
search: Element to replace
replace: New element
"""
