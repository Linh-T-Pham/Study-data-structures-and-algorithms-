
class doublylinkedlist():
    def __init__(self):
        self.head = None
        self.tail = None

#SEARCHING METHOD
# Search value in the given ll
# in the doubled ll, I can start at the head or the tail 
# traverse the ll then do the check --> use while 
# Current node is not Null or None
# if the current node is not  the given node
# set the pointer to  currentnode.next then compare to the given node
#until hit None then we return False (end 10:49)
def search_node(self, value):
    node = self.head
    while node is not None and node.value != value: 


#REMOVING Node with value METHOD
# Remove a given node 
# when we remove a node, take that node and remove the pointers
#(update the .next and .prev)
# update pointers in the correct order. first check if node before.next
# is not Null. if it not Null(15:03)
# we also need to check if we are dealing with the head or tail when
# removing a node 
# if we are dealing with the head, set the head of the ll to the next node
# of the node we are removing(16:30) 


# Inserting method 
# insert a node before a given node. 