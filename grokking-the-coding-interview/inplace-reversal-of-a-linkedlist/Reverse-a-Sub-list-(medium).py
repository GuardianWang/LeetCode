"""
LC 92
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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


def reverse_sub_list(head, p, q):

  prev = Node(0, head)  # the node before p
  cnt = 0
  while cnt != p - 1:
    prev = prev.next
    cnt += 1
  left = prev
  p_node = prev.next
  mid = p_node
  cnt = p
  while cnt != q + 1:
    right = mid.next
    mid.next = left
    left, mid = mid, right
    cnt += 1
  prev.next = left
  p_node.next = mid
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""
