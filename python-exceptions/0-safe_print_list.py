#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            count += 1
        except Exception as e:
            pass
    print("")
    return (count)
