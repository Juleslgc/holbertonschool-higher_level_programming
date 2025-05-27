#!/usr/bin/python3
"""
This is the "task_04_abc" modulo.
It contains the class :
Fish
Bird
FlyingFish
It contains the function :

"""


class Fish:
    """
    Class Fish
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Class Bird
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Subclass FlyingFish
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
