#!/usr/bin/python3

def pow(a, b):
    if a == 0:
        return 0
    if a != 0 and b == 0:
        return 1
    product = 1

    if b > 0:
        for num in range(b):
            product = product * a
        return product

    quotient = 1
    b = b * -1

    for num in range(b):
        quotient = quotient / a
    return quotient
