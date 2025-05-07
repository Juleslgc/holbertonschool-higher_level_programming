#!/usr/bin/python3
import sys


def main(*argv):
    len_argv = len(sys.argv) - 1
    i = 0

    if len_argv == 1:
        print(f"{len_argv} arguments:")
    elif len_argv == 0:
        print(f"{len_argv} arguments.")
    else:
        print(f"{len_argv} arguments:")

    for a in sys.argv:
        if i != 0:
            print(f"{i}: {a}")
        i += 1


if __name__ == "__main__":
    main()
