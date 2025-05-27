#!/usr/bin/python3
"""
This is the "task_00_abc" modulo.
It contains the class :
Animal
Dog
Cat
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Aniaml
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass Dog
    """
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """
    Subclass Cat
    """
    def sound(self):
        return ("Meow")
