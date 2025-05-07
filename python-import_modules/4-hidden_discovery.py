#!/usr/bin/python3
import hidden_4


def main():
    name = dir(hidden_4)
    for i in range(len(name)):
        if name[i][0] != '_':
            print("{}".format(name[i]))


if __name__ == "__main__":
    main()
