#!/usr/bin/python3
if __name__=="__main":
    import sys

    args = sys.argv
    len_args = len(args) - 1

    if len_args > 1:
        print("{} arguments:".format(len_args))
        for index in range(1, len_args + 1):
            print("{}: {}".format(index, args[index]))
    elif len_args == 0:
            print("{} arguments:".format(index, args[index]))
    else:
        print("{} argument:".format(index))
        print("{}: {}".format(len_args, args[1]))
