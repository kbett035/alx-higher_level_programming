#!/usr/bin/python3
# Wyclife Kimutai <kimutaiwyclife6@gmail.com>
# 1-search_replace.py



def search_replace(my_list, search, replace):
    """Replace occurrences of an element by another in a new list."""
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
