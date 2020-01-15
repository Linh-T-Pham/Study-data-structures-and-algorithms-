# A Table is given. Table is similar to a python list. You can choose the length 
# for the list

# Everytime we add items (key, value) pairs, (key,value) pairs have to go in the 
# table

# A hash function requires a key

# Pass the key value to the has funciton to find the idex -->
# add to the has table using the idex


# Solution:

# Data collision: Using LinkedlistNode to account for data collision 



class Node:
    """"Create Class Node """
    def _init_(self, key, value):

        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def _init_(self):
        self.capacity = 11
        self.buckets =[None]*self.capacity

    def hashKey(key):
        return hash(key) % self.capacity

""""
>>> key = 'apple'
>>> key
'apple'
>>> hash(key)
1512600610774552938
>>> cap = 11
>>> h = hash(key)
>>> h % cap
1
>>> h % cap
1
>>> key = 'banaba'
>>> h % cap
1
>>> h = hash(key)
>>> h % cap
6
>>> 
"""

