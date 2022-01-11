"""
LC 23
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""
from heapq import *


class ListNode:
  def __init__(self, value):
    self.val = value
    self.next = None


def merge_lists(lists):
  if not lists:
    return None 

  step = 1
  while step < len(lists):
    for start in range(0, len(lists) - step, 2 * step):
      lists[start] = merge2(lists[start], lists[start + step])
    step *= 2

  return lists[0]


def merge2(node1, node2):
  head = ListNode(0)
  res = head
  while node1 and node2:
    if node1.val < node2.val:
      res.next = node1 
      node1 = node1.next 
    else:
      res.next = node2 
      node2 = node2.next 
    res = res.next

  if node1:
    res.next = node1 
  elif node2:
    res.next = node2
    
  return head.next 


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result is not None:
    print(str(result.val) + " ", end='')
    result = result.next


main()


"""
Time O(NlogK): logK level
Space O(1)
"""

