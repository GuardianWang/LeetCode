"""
LC 632
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
Example 1:
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
Example 2:
Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
"""
from heapq import *


def find_smallest_range(lists):
  # keep track of min and max
  heap = []
  M = -float('inf')
  for i, l in enumerate(lists):
    heappush(heap, (l[0], i, 0))
    M = max(M, l[0])
  min_diff = M - heap[0][0]
  ranges = [heap[0][0], M]

  while len(heap) == len(lists):
    val, i, j = heappop(heap)
    if j + 1 < len(lists[i]):
      heappush(heap, (lists[i][j + 1], i, j + 1))
      M = max(M, lists[i][j + 1])
      if M - heap[0][0] < min_diff:
        min_diff = M - heap[0][0]
        ranges = [heap[0][0], M]

  return ranges


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()


"""
Time O(NlogK)
Space O(K)
"""

