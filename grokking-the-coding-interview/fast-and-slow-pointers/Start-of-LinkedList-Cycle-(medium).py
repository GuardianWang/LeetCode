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
    # length of cycle
    cnt = 0
    while True:
        slow = slow.next 
        cnt += 1
        if slow is fast:
            break 
    # find cycle start
    # fast will go through all nodes
    # slow will go through non-cyclic nodes
    slow, fast = head, head 
    for _ in range(cnt):
        fast = fast.next 
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

