2 -> 1 -> 3 -> 9 -> 10
#           |
#           4 -> 5 -> 8
#                |
#                6 -> 7
# 
# 2 -> 1 -> 3 -> 4 -> 5-> 6-> 7 -> 8 -> 9 -> 10
#
#               2
#                \
#                 1
#                  \
#                   3
#                  / \
#                 4   9
#                  \   \
#                   5   10
#                  / \
#                 6.  8
#                  \
#                   7
#
# P(root) := print(root.value); P(root.left); P(root.right)
# P(empty) := 



class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def P(node: Node) -> None:
    if node is None:
        return 

    print(node.val)
    P(node.left)
    P(node.right)


P(Node(2, left=Node(1), right=Node(3)))
