#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args)

    if num_args == 1:
        print("{} arguments.".format(num_args - 1))
    else:
        if num_args == 2:
            print("{} argument:".format(num_args - 1))
        else:
            print("{} arguments:".format(num_args - 1))

        for num in range(1, num_args):
            print("{}: {}".format(num, args[num]))
