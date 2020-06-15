 # Calculate the height of binary tree
 #     5
 #    / \
 #   6   2
 #  /  \  
 # 7   10

class Node:
    def__init__(self, x):
        self.value = x
        self.left = None
        self.right = None 

def find_height_BT(node):
    if node is None:
        return -1 

    left_height = find_height_BT(node.left)
    right_height = find_height_BT(node.right)

    return 1 + max(left_height. right_height)





tree = Node(5)
tree.node.left = Node(6)
tree.node.right = Node(2)
tree.node.left.left = Node(7)
tree.node.right.right = Node(10)