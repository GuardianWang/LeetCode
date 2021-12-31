"""
LC 61
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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


def rotate(head, rotations):
  if head is None:
    return head
  l, end = list_len(head)
  rotations %= l 
  if rotations == 0:
    return head

  sent = Node(0, head)
  prev = sent
  for _ in range(l - rotations):  # rotations back to the front
    prev = prev.next 
  start = prev.next 
  end.next = head 
  prev.next = None 

  return start


def list_len(head):
  prev = Node(0, head)
  cnt = 0
  while prev.next:
    cnt += 1
    prev = prev.next
  return cnt, prev


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()


"""
Time O(N)
Space O(1)
"""

