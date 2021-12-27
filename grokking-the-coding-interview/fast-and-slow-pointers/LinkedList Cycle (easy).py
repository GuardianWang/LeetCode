"""
LC 141
write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
    slow, fast = head, head 

    while True:
        try:
            slow = slow.next 
            fast = fast.next.next 
        except:  # come to an end
            return False
        if slow == fast:
            return True


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))  # F

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))  # T

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))  # T


main()


"""
Time O(N)
Space O(1)
"""

