#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguc = len(argv) - 1
    if arguc == 0:
        print("0 arguments.")
    elif arguc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguc))
    for i in range(arguc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]]))
