#!/usr/bin/python3
def no_c(my_string):
    p = my_string.translate({ord(r): None for r in 'cC'})
    return p
