"""
Reverse the first ‘k’ elements of a given LinkedList.
"""


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


def reverse_sub_list(head, k):
  cnt = 0
  left, mid = None, head 
  while cnt != k:
    right = mid.next 
    mid.next = left 
    left, mid = mid, right 
    cnt += 1
  head.next = mid 
  return left
    

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 5)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""

