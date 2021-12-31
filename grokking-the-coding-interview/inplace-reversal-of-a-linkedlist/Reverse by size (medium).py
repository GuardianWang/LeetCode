"""
Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:

If ‘n’ is even, reverse the list in a group of n/2 nodes.
If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
"""


class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.val, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, l: int, r: int):
  cnt = 0
  sent = Node(0, head)
  prev = sent 
  while cnt != l - 1:
    prev = prev.next
    cnt += 1

  cnt = l 
  l_node = prev.next 
  mid = l_node
  left = None 
  while cnt <= r:
    right = mid.next 
    mid.next = left 
    left, mid = mid, right 
    cnt += 1
  prev.next = left 
  l_node.next = mid
  return sent.next, l_node  # need to change l_node.next
  

def reverse_group(head, n):
  head, tail = reverse_sub_list(head, 1, n // 2)
  if n % 2 == 0:
    reverse_sub_list(tail, 2, n // 2 + 1)
  else:
    reverse_sub_list(tail.next, 2, n // 2 + 1)
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_group(head, 5)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""

