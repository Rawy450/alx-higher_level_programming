#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    q = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (q[0] + b[0], q[1] + b[1])
