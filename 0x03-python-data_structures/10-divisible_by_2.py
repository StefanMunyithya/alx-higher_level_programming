#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    div_by_2 = []
    for num in my_list:
        if num % 2 == 0:
            div_by_2.append(True)
        else:
            div_by_2.append(False)
    return (div_by_2)
