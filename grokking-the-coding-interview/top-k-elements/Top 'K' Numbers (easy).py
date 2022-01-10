"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""
from heapq import *


def find_k_largest_numbers(nums, k):
    h = []
    for n in nums:
        if len(h) < k:
            heappush(h, n)
        elif h[0] < n:
            heapreplace(h, n)
    return h


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()


"""
Time O(NlogK)
Space O(K)
"""

