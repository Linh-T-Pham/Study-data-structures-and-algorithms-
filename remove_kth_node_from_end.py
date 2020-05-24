""" Write a function that takes in the head of Singly LL and 
    interger k and removes the kth node from the end of the list.

    Each linkedlist node has integer value as well as a next node pointing to the
    next node in the list or to None/Null if its the tail of the list

    You can assume that the input linked list will always have at least k nodes

    REMOVE KTH NODE FROM THE END OF THE LIST
    2->4->6->8
    K=2
    OUTPUT: 2->4->8
"""



class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

        
def return_kth_node(head, k):
    pointer1 = pointer2 = head

    if not head:
        print("Invalid linked list")
        return


    count = 0
    while count < k:
        pointer1 = pointer1.next
        count += 1

    
    while pointer1.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer2.data

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


print(return_kth_node(head, 3))
         
        