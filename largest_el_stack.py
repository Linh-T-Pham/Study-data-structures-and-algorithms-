# You want to be able to access the largest element in a stack. 
# You've already implemented this Stack class:


class Stack(object):

    def _init_(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)