#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    alpha = tuple_a + (0, 0)
    beta = tuple_b + (0, 0)
    new = alpha[0] + beta[0], alpha[1] + beta[1]
    return new
