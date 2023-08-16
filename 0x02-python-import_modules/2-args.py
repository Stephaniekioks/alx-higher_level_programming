#!/usr/bin/python3
if __name__ == "__main__":
    """print number and list of arguments"""
    import sys

    i = len(sys.argv) - 1

    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(i))

        for i in range(count):
                    print("{}: {}".format(i + 1, sys.argv[i + 1]))
