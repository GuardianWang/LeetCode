"""
LC 347
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""
from heapq import *


def find_k_frequent_numbers(nums, k):
  nums.sort()
  nums.append(nums[-1] + 1)  # make sure go through the last value
  h = []
  l = 0
  for r, n in enumerate(nums):
    if nums[l] != n:
      freq = r - l
      if len(h) < k:
        heappush(h, (freq, nums[l]))
      elif freq > h[0][0]:
        heapreplace(h, (freq, nums[l]))
      l = r

  return [x[1] for x in h]


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()


"""
Time O(NlogN)
Space O(N): sort
"""

