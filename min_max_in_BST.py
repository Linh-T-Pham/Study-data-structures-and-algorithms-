"""Find the min and max values in BST"""

#     10
#    /   \
#   5     16
#  / \   /  \
# 3   1 11   18



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

def find_min(root):
    if root is None:
        return -1 

    while root.left != None:
        node = node.left 