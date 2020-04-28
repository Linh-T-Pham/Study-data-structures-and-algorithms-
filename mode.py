"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""
     """Find the most frequent num(s) in nums."""

    # START SOLUTION

    # Make dictionary of {num:frequency}

    num_count = {}

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    # Find the *count* of highest letter

    highest_count = max(num_count.values())

    # For every number with that count, add to set of mode

    mode = set()

    for num, count in num_count.items():
        if count == highest_count:
            mode.add(num)

    return mode


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
