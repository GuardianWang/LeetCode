"""
LC 373
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.
Example 1:
Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.
Example 2:
Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]
"""
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  i1, i2 = 0, 0
  visited = set([(i1, i2)])
  heap = [(-nums1[i1] - nums2[i2], i1, i2)]
  res = []
  for _ in range(min(k, len(nums1) * len(nums2))):
    s, i1, i2 = heappop(heap)
    res.append([nums1[i1], nums2[i2]])
    if (i1 + 1 < len(nums1) and (i1 + 1, i2) not in visited):
      visited.add((i1 + 1, i2))
      heappush(heap, (-nums1[i1 + 1] - nums2[i2], i1 + 1, i2))
    if (i2 + 1 < len(nums2) and (i1, i2 + 1) not in visited):
      visited.add((i1, i2 + 1))
      heappush(heap, (-nums1[i1] - nums2[i2 + 1], i1, i2 + 1))
  return res
  

def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()


"""
T = min(MN, K)
Time O(TlogT)
Space O(T)
"""

