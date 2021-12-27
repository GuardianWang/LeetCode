"""
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slow, fast = head, head 
    while True:
        slow = slow.next 
        fast = fast.next.next 
        if slow is fast:
            break
    cnt = 0
    while True:
        slow = slow.next 
        cnt += 1
        if slow is fast:
            return cnt


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))  # 4

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))  # 3


main()


"""
Time O(N)
Space O(1)
"""

