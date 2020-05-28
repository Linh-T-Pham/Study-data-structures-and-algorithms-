""" Merge Linked Lists
    Write a function that takes in the heads of two singly Ll that are 
    in sorted order, respectively. The function should merge the lists
    in place(i.e, it should not create a brand new list and return the head
    of the merged list; the merged list should be in sorted order)

    Each linked list node has an integer value as well as a next node pointing
    to the next node in the list or to None/Null if its the tail of the list.

    You can assume that input linked lists will always have at least one node;
    in other words, the heads will be never be None/Null. 


"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # last item 
        


# if 
# h1 > h2
#     insert head_two.data before head_one.data
#      pointer2 += 1        
# else:
# h1 < h2:
#     insert head_two.data after head_one.data
        


# head_one 1-2-6-7-8
# head_two 4-5-10-11-12
# out put 4
"""
"""

def merge_ll(head1, head2):
    p1prev = None 
    p1 = head1
    p2 = head2

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            # p1 = p1.next
            p1prev = p1
            p1 = p1.next

        elif p1.value > p2.value: 
            if p1 is not None: # What happen when P1 is not None 
                p1prev.next = p2 # because p1pev is None so it does not make sense 
                                # to assign p1prev = p2 
        p1prev = p2
        p2 = p2.next 
        p1prev.next = p1

    if p1 is None:
        p1prev.next = p2
    
    if head1.value < head2.value:
        return head1
    else:
        return head2









    

    

      
  
        
head_one = Node(2)
head_one.next = Node(6)
head_one.next.next = Node(7)
head_one.next.next.next = Node(8)

head_two = Node(1)
head_two.next = Node(3)
head_two.next.next = Node(4)
head_two.next.next.next = Node(5)
head_two.next.next.next.next = Node(9)
head_two.next.next.next.next.next = Node(10)










# def merge_ll(head_one, head_two):
    
#     point1 = head_one
#     point2 = head_two
#     point1_prev = None # previous node in the first linked list 
    
#     # 1 -> 6 ->7
#     while point1 is not None and point2 is not None: 
#         if point1 < point2:
#             point1_prev = point1 #none #6
#             point1 = point1.next #1 #7
#         else:
#             # p2 comes before p1 
#             # so p1prev shoudl point to p2
#             if point1_prev is not None:
#                 point1_prev = point2 
#             point_prev = point1 # before overwite p2 
#             point2 = point2.next
#             point1_prev.next = point1


