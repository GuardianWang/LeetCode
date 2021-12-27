"""
LC 234
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # find middle or right middle 
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next 
        slow = slow.next 

    # reverse 
    tail = reverse(slow)

    # check 
    p1 = head 
    p2 = tail
    while p2 is not None:
        if p2.value != p1.value:
            return False
        p2 = p2.next
        p1 = p1.next 

    # revert
    mid = reverse(tail)

    return True 


def reverse(start):
    # reverse 
    mid = start
    left = None
    while mid is not None:
        right = mid.next
        mid.next = left 
        left = mid
        mid = right 
    return left 


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))  # T

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))  # F

    head = Node(0)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))  # T

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))  # T

    head.next.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))  # F


main()


"""
Time O(N)
Space O(1)
"""

