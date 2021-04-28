#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    l = len(argv) - 1

    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
        for i in argv:
            if count:
                print("{:d}: {:s}".format(count, i))
            count += 1
    else:
        print("{:d} arguments:".format(l))
        for i in argv:
            if count:
                print("{:d}: {:s}".format(count, i))
            count += 1
