
"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

  For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""

Create a function take 2 arguments (char, array, start=0)
array is not empty
base case: 
1. found it --> return idx
2. reached end of list, and didn't find it --> return None



def recursive_idx(needle, haystack, start=0):
    if start == len(haystack):
        return None
    
    if needle == haystack[start]:
        return start
    
    # start += 1
    return recursive_idx(needle, haystack, start + 1)


# for recusive call, we start with default agrument and then we increment it so 
# it will be just On time and space
# n is the number of recursive calls and the length of the list 
