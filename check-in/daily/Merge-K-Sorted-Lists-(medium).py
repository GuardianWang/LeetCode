"""
LC 23
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        step = 1
        while step < len(lists):
            for i in range(0, len(lists), 2 * step):
                if i + step < len(lists):
                    lists[i] = self.merge2(lists[i], lists[i + step])
            step *= 2
        return lists[0]
    
    def merge2(self, n1, n2):
        sent = p = ListNode()
        while n1 and n2:
            if n1.val < n2.val:
                p.next = n1
                n1 = n1.next
            else:
                p.next = n2
                n2 = n2.next
            p = p.next
        if n1:
            p.next = n1
        elif n2:
            p.next = n2
        return sent.next


"""
Time O(Nlogk)
Space O(1)
"""      
