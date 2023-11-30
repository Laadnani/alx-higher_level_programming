#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}" .format(argv[1]))
    else:
        print("{}: arguments:" .format(len(argv) - 1))
        n = 1
        while n < len(argv):
            print("{}: {}" .format(n, argv[n]))
            n += 1
