# You want to be able to access the largest element in a stack. 
# You've already implemented this Stack class:


class Stack(object):

    def _init_(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""

        # if the stack is empty, return None
        # it would also be reasonable to throw an exception

        if not self.items:
            return None

        return self.items.pop()

    def peek(self):

        """Return the last item without removing it"""

        if not self.items:
            return None

        return self.items[-1]


# Use your Stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack.get_max() should not remove the item
# Your stacks should contain only integers 

# What if we push several items in increasing numberic order like(1,2,34,...), 
# so that there is a new max after each push()? What if we then pop() each of these
# items off, so that there is a new max after each pop()? The algorithm should not 
# pay a steep cost in these edge cases

# You should be able to get a runtim of O(1) for push(), pop(), and get_max()

# A just-in-time approach is to have get_max() simply walk through the stack(poping all
# the elements off and then pushing them back on ) to find the max element. 
# This takes O(n) time for each call to get_max().But we can do better

# To get O(1) time for get_max(), we could store the max integer as a member variable
#(call it max). But how would we keep it up to date?

# For every push(), we can check to see if the item being pushed is larger than the current
# max, assigining it as our new max if so. But what happens when pop() the current max?
# We could re-compute the current max by walking through our stack in O(n) time. So 
# our worst-case runtime for pop() would be O(n). We can do better

# What if when we find a new current max(new_max), instead of overwriting the old one
#(old_max) we held onto it, so that once new_max was poppped off our stack we would
# know that our max was back to old_max?

# What data structure should we store our set of maxes in? We want sth where the last
# item we put in is the first item we get out("last in, first out")
# We can store our maxes in another stack!

# SOLUTION    

# We define 2 new stacks within our MaxStack class-stack holds all of our integers
# and maxes_stack holds our"maxima". We use maxes_stack to keep our max up to date in 
# constant time as we push() and pop()

# 1. Whether we push() a new item, we check to see if it's greater than
# or equal to the current max, which is at the top of maxes_stack. If it is, we also
# push() it onto maxes_stack

class MaxStack(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack"""
        self.stack.push(item)

        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek()
            self.maxes_stack.push(item)
    
    def pop(self):

        """Remove and return the top item from our stack"""
        item = self.stack.pop()

        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item 

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack"""
        return self.maxes_stack.peek()

# Complexity
# O(1)O(1) time for push(), pop(), and get_max(). O(m)O(m) additional space, where mm is the number of operations performed on the stack.

# Bonus
# Our solution requires O(m)O(m) additional space for the second stack. But do we really need it?

# Can you come up with a solution that requires O(1)O(1) additional space? (It's tricky!)

# What We Learned
# Notice how in the solution we're spending time on push() and pop() so we can save time on get_max(). That's because we chose to optimize for the time cost of calls to get_max().

# But we could've chosen to optimize for something else. For example, if we expected we'd be running push() and pop() frequently and running get_max() rarely, we could have optimized for faster push() and pop() methods.

# Sometimes the first step in algorithm design is deciding what we're optimizing for. Start by considering the expected characteristics of the input.


