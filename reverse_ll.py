from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
  if head is None or head.next is None:
    return head

  previous, current, next = None, head, None
  while current is not None:
    next = current.next  # temporarily store the next node
    current.next = previous  # reverse the current node
    previous = current  # before we move to the next node, point previous to the current node
    current = next  # move on the next node
  return previous


# def main():
#   head = Node(2)
#   head.next = Node(4)
#   head.next.next = Node(6)
#   head.next.next.next = Node(8)
#   head.next.next.next.next = Node(10)

#   print("Nodes of original LinkedList are: ", end='')
#   head.print_list()
#   result = reverse(head)
#   print("Nodes of reversed LinkedList are: ", end='')
#   result.print_list()


# main()


def reverselinkedlist(head):
    current = head # (3-4-5-6-None)
    next = None
    previous = None
    
    while current:
        next = current.next # save the value of current.next for later use
        current.next = previous # replace the value current.next with previous 
        previous = current 
        current = next # go back to the initial value of current.next
    
        
    return previous


    
    """
    3->4->5->6->None
    
    1st iteration
    next = 4 -> 5 -> 6 -> None
    current.next = None # 3->None
    previous = 3 -> None
    current = 4 -> 5 -> 6 -> None

    2nd iteration
    next = 5 -> 6 -> None
    current.next = 3 -> None # current + current.next 4-3-none
    previous = 4 -> 3 -> None
    current = 5 -> 6 -> None
        
    3rd iteration
    next = 6 -> None
    current.next = 4 -> 3 -> None 
    previous = 5 -> 4 -> 3 -> None
    current = 6 -> None
    
    4th iteration
    next = None
    current.next = 5 -> 4 -> 3 -> None 
    previous = 6 -> 5 -> 4 -> 3 -> None
    current = None
    
    """