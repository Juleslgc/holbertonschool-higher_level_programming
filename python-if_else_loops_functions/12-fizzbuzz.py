#!/usr/bin/python3
def fizzbuzz():
    i = 3
    j = 5
    for num in range(1, 101):
        if (num % i) == 0 and (num % j) == 0:
            print("FizzBuzz", end=" ")
        elif (num % i) == 0:
            print("Fizz", end=" ")
        elif (num % j) == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(num), end=" ")
