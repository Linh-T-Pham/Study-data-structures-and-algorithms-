"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> binary_search(100) <= 7
    1

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_searches = 0
    guess = None


    higher_than = 0
    lower_than = 101

    while guess != val:
        num_searches += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess
        elif val < guess:
            lower_than = guess 

    return num_searches





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n")


# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

'''
naive solution to loop through list, return index of element that matches the target
if exiting loop then return -1 for not found in list

binary search solution:
hold index in variable. set it to the length of the list // 2
loop until
base case is
'''


def search(nums, target):
    left = 0
    right = len(nums) - 1
    center = (right + left) // 2
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    while left + 1 < right:
        if nums[center] == target:
            return center
        if nums[center] < target:
            left = center
        else:
            right = center
        center = (right + left) // 2
    return -1

print(search([-1,0,3,5,9,12], -1))
print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
print(search([-1,0,3,5,9,12], 0))
print(search([-1,0,3,5,9,12], 12))


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             pivot = left + (right - left) // 2
#             if nums[pivot] == target:
#                 return pivot
#             if target < nums[pivot]:
#                 right = pivot - 1
#             else:
#                 left = pivot + 1
#         return -1

