"""
LC 287
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""
class Solution:
    def findDuplicate(self, nums) -> int:
        M = len(nums)
        for n in nums:
            nums[n % M - 1] += M
        M2 = 2 * M
        for i, n in enumerate(nums):
            if n > M2:
                res = i + 1
            nums[i] %= M
        return res


"""
Time O(N)
Space O(1)
"""

