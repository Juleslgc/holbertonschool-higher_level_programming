#!/usr/bin/python3
"""
This is the "task_02_abc" modulo.
It contains the class :
VerboseList
It contains the function :

"""


class VerboseList(list):
    """
    Subclass VerboseList
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
