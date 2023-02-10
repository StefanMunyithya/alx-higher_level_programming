#!/usr/bin/python3

def no_c(my_string):
    if len(my_string) == 0:
        return my_string
    new_string = ""
    for char in my_string:
        if (char == 'c') or (char == 'C'):
            continue
        new_string = new_string + char
    return (new_string)
