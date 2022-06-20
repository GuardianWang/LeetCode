"""
LC 143
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example 1:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
Example 2:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if not head.next or not head.next.next:
        return
    # middle or right middle 
    slow, fast = head, head 
    pre = Node(0, next=head)
    while fast is not None and fast.next is not None:
        slow = slow.next 
        pre = pre.next
        fast = fast.next.next 
    pre.next = None
    # reverse 
    tail = reverse(slow)
    p1, p2 = head, tail
    while p1 and p2:
        # swap p1 and p2
        p1.next, p2, p1 = p2, p1.next, p2


def reverse(start):
    left, mid = None, start 
    while mid is not None:
        right = mid.next 
        mid.next = left 
        left, mid = mid, right
    return left


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    head.next.next.next.next.next.next = Node(14)
    reorder(head)
    head.print_list()


main()


"""
Time O(N)
Space O(1)
"""
