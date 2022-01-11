"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:
Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""
from heapq import *


def find_Kth_smallest(lists, k):
  h = [(l[0], i, 0) for i, l in enumerate(lists) if l]
  heapify(h)
  for _ in range(k):
    val, i, j = h[0]
    if j + 1 < len(lists[i]):
      heapreplace(h, (lists[i][j + 1], i, j + 1))
    else:
      heappop(h)
  return val


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()


"""
Time O(KlogM), M is len(lists)
Space O(M)
"""

