"""Given two lists, concatenate the second list at the end of the first.

For example, given ``[1, 2]`` and ``[3, 4]``::

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

It should work if either list is empty::

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
"""

# solution 1

# def concat_lists(list1, list2):
#     """Combine lists."""

#     for item in list2:
#         list1.append(item)
#     return list1

#solution 2

def concat_lists(list1, list2):
    """Concatenate the lists"""

    return (list1 + list2)
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
