"""
LC 25
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

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


def reverse_every_k_elements(head, k):
  l = list_len(head)
  sent = Node(0, head)
  head = sent
  for _ in range(l // k):
    # returned head is the end of reversed list
    # use this to make sure time is O(N)
    head = reverse_sublist(head, 2, k + 1)
  return sent.next


def list_len(head):
  cnt = 0
  while head:
    head = head.next
    cnt += 1
  return cnt


def reverse_sublist(head, l, r):
  cnt = 0
  sent = Node(0, head)
  prev = sent
  while cnt != l - 1:
    prev = prev.next
    cnt += 1
  l_node = prev.next

  left, mid = prev, l_node
  cnt = l
  while cnt <= r:
    # left will finally become r_node
    if mid is None:
      return None
    right = mid.next
    mid.next = left
    left, mid = mid, right
    cnt += 1
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
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""

