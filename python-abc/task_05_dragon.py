#!/usr/bin/python3
"""
This is the "task_05_dragon" modulo.
It contains the class :
SwimMixin
FlyMixin
Dragon
It contains the function :

"""


class SwimMixin:
    """
    Class Swim mixin
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Class Fly mixin
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class Dragon
    """
    def roar(self):
        print("The dragon roars!")
