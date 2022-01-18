"""
LC 1
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from collections import defaultdict


class Solution:
    def twoSum(self, nums, target: int):
        n2i = defaultdict(list)
        for i, n in enumerate(nums):
            n2i[n].append(i)

        for n in nums:
            n2 = target - n
            if n2 in nums:
                if n != n2:
                    return [n2i[n][0], n2i[n2][0]]
                if n == n2 and len(n2i[n]) > 1:
                    return n2i[n][:2]


"""
Time O(N)
Space O(1)
"""

