#!/usr/bin/python3
"""
This is the "0-square" modulo.
It contains the class :
square
"""


class Square:
    """
    create square class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) is not tuple and len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value[0]) is not int and len(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.__size):
                print('_' * self.__position[0], end="")
                print('#' * self.__size)
