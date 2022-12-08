#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    prints a dictionary by ordered keys. keys assumed to be strings
    """
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
