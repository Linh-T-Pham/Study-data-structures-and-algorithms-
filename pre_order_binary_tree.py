"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3305/

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# Input: [8,5,1,7,10,12]    --> [1,5,7,8,10,12]
# Output: [8,5,10,1,7,null,12]

        8 
    5       10
1     7   null  12

dp_0 = [8]
dp_1 = [5, 10]
dp_2 = [1,7,12]

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder):
    if not preorder:
        return None

    left_nodes = []
    right_nodes = []
    root = preorder[0]

    root_node = TreeNode(root)

    for i, n in enumerate(preorder, start=1):
        if n < root:
            left_nodes.append(n)
        elif n > root:
            right_nodes.append(n)
    

    root_node.left = bstFromPreorder(left_nodes)
    root_node.right = bstFromPreorder(right_nodes)

    return root_node



# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         root = TreeNode(preorder[0])
#         i = 1
#         while i<len(preorder) and  preorder[i] < root.val:
#             i+=1
#         root.left = self.bstFromPreorder(preorder[1:i])
#         root.right = self.bstFromPreorder(preorder[i:])
#         return root

# i=2
# root = 8
# root.left = recur w/ [5,1,7]
# root.right = recur w/ [10,12]

# newtree = bstFromPreorder([8,5,1,7,10,12])
# print(newtree.val)
# print(newtree.right.left)



