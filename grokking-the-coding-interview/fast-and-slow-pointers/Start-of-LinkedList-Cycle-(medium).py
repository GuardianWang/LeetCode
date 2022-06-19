"""
LC 142
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head 
    # find a node in cycle
    while True:
        try:
            slow = slow.next 
            fast = fast.next.next 
        except:
            return None
        if slow is fast:
            break
    # https://leetcode.com/problems/linked-list-cycle-ii/solution/
    # note: F = h (mod C) because h = F % C
    # they meet at C - h
    # after F steps, C - h + F = 0 (mod C) because F = h (mod C)
    # don't need length of cycle
    # both start from head!
    slow = head
    while slow is not fast:
        slow = slow.next 
        fast = fast.next 
    return slow
        
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))  # 3

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))  # 4

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))  # 1


main()


"""
Time O(N)
Space O(1)
"""

