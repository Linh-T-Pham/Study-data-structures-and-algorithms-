
# https://fellowship.hackbrightacademy.com/materials/challenges/make-bst/index.html

""" pseudocode
[1,2,3,4,5]

    [3]
[1,2]  [4,5]
        3
      2   4
     1      5

[1,2,3]

  [2]
[1] [3]

base case = list of len 1   
  return item in list

recursive case:
  middle --> parent node  // [1,2,3,4,5] --> len(lst)//2
  left = [:middle]
  right = [middle+1:]

"""
class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

        
def make_bst(nums):

    if not nums:
        return None
        
    # if len(nums) == 1:
    #     return nums[0]
    
    parent_node_idx = len(nums)//2
    parent_node = BinaryNode(nums[parent_node_idx])

    parent_node.left = make_bst(nums[:parent_node_idx])
    # parent_node.left = BinaryNode(left)
    
    parent_node.right = make_bst(nums[parent_node_idx+1:])
    # parent_node.right = BinaryNode(right)

    return parent_node


tree = make_bst([1,2,3,4,5,6,7])
"""
        4
     /-----\
    2      6
   / \    / \
  1   3  5   7
"""
print(f'Root node: {tree.data}')  
print(f'Root node left child: {tree.left.data}')
print(f'Root node left right child: {tree.left.right.data}')

