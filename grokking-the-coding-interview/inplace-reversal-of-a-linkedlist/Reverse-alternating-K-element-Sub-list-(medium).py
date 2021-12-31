"""
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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


def reverse_alternate_k_elements(head, k):
  sent = Node(0, head)
  head = sent 
  l = list_len(head)
  head = reverse_sublist(head, 2, k + 1)
  for _ in range((l - k) // (2 * k)):
    head = reverse_sublist(head, k + 2, 2 * k + 1)
  return sent.next 


def list_len(head):
  cnt = 0
  while head:
    cnt += 1
    head = head.next 
  return cnt


def reverse_sublist(head, l, r):
  sent = Node(0, head)
  prev = sent 
  for _ in range(l - 1):
    prev = prev.next
  l_node = prev.next 

  left, mid = prev, l_node 
  for _ in range(r - l + 1):
    right = mid.next 
    mid.next = left 
    left, mid = mid, right 
  # left is the last to reverse 
  # after reversing, l_node becomes the last
  prev.next = left 
  l_node.next = mid 
  return l_node


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)
  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""

