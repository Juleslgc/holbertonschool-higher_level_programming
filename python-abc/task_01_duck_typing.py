#!/usr/bin/python3
"""
This is the "task_01_abc" modulo.
It contains the class :
Shape
Circle
Rectangle
It contains the function :
shape_info
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Class Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Subclass Circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Subclass Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(arg):
    print("Area: {}".format(arg.area()))
    print("Perimeter: {}".format(arg.perimeter()))
