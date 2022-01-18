"""
LC 462
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
"""
from random import randint 


class Solution:
    def minMoves2(self, nums) -> int:
        # find median
        # if the value is > or < median 
        # more values will increase than the other half decreasing values
        target = self.find_median(nums)
        return int(sum(map(lambda x: abs(target - x), nums)))

    def find_median(self, nums):
        l, r = 0, len(nums) - 1
        m = (l + r) >> 1
        while l <= r:
            p = self.partition(nums, l, r)
            if p < m:
                l = p + 1
            elif p > m:
                r = p - 1
            else:
                return nums[p]

    def partition(self, nums, l, r):
        p = randint(l, r)
        self.swap(nums, p, r)
        for i in range(l, r):
            if nums[i] < nums[r]:
                self.swap(nums, l, i)
                l += 1
        self.swap(nums, l, r)
        return l

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

        
"""
Time O(N)
Space O(1)
"""

