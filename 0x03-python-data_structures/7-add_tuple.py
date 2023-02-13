#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0

    for idx in range(2):
        if idx == 0:
            if len(tuple_a) > idx:
                sum1 += tuple_a[idx]
            if len(tuple_b) > idx:
                sum1 += tuple_b[idx]
        else:
            if len(tuple_a) > idx:
                sum2 += tuple_a[idx]
            if len(tuple_b) > idx:
                sum2 += tuple_b[idx]
    return (sum1, sum2)
