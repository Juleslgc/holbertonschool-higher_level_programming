#!/usr/bin/python3
import sys


def main(*argv):
    len_argv = len(sys.argv)
    sum = 0

    if len_argv > 1:
        for a in sys.argv:
            if a != sys.argv[0]:
                sum += int(a)
    print(sum)


if __name__ == "__main__":
    main()
