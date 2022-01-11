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
  # save freq in dict 
  freqs = {}
  for n in nums:
    if n not in freqs:
      freqs[n] = 1
    else:
      freqs[n] += 1

  h = []
  l = 0
  for n, freq in freqs.items():
    if len(h) < k:
      heappush(h, (freq, n))
    elif freq > h[0][0]:
      heapreplace(h, (freq, n))

  return [x[1] for x in h]


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()


"""
Time O(NlogK)
Space O(N)
"""

