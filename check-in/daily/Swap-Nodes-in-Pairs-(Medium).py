"""
LC 24
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapPairs(self, head):
        sent = ListNode(next=head)
        prev = sent
        while head:
            prev, head = self.swap(prev, head)
        return sent.next
        
    def swap(self, prev, head):
        # swap head and head.next 
        # return head and head.next.next 
        if not (head and head.next):
            return head, None
        second = head.next 
        head.next = second.next 
        second.next = head 
        if prev:
            prev.next = second
        return head, head.next
        

"""
Time O(N)
Space O(1)
"""
