#!/usr/bin/python3
"""
This is the "task_03_countediterator" modulo.
It contains the class :
CountedIterator
It contains the function :

"""


class CountedIterator:
    """
    Class CountedIterator
    """
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items.")
