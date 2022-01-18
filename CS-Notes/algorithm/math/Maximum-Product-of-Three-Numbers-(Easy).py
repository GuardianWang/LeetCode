"""
LC 628
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""
from heapq import *


class Solution:
    def maximumProduct(self, nums) -> int:
        # smallest 2 and largest 3
        # 3 largest:
        # [+ + +]  this three 
        # [- + +]  m2 * l[2]
        # [- - +]  max(m2*l[2], l3)
        # [- - -]  this three 
        m2 = []  # map heap
        l3 = []  # min heap
        for n in nums:
            if len(l3) < 3:
                heappush(l3, n)
            elif n > l3[0]:
                heapreplace(l3, n)

            if len(m2) < 2:
                heappush(m2, -n)
            elif n < -m2[0]:
                heapreplace(m2, -n)
        return max(-m2[0] * -m2[1] * max(l3),
                   l3[0] * l3[1] * l3[2])


"""
Time O(N)
Space O(1)
"""

