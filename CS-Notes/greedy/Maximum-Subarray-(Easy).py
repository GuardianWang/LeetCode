"""
LC 53
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
class Solution:
    def maxSubArray(self, nums) -> int:
        cur = 0
        M = nums[0]
        for n in nums:
            # look on a subarray as one value
            # if cur > 0, any subsubarray ending at the same position
            # has smaller sum 
            # By contradiction, if has larger sum, then the prefix has negative sum
            # and would have been discarded
            cur = max(cur + n, n)
            M = max(M, cur)
        return M

    def divide_conquer(self, nums, l, r):
        # T(n) = 2T(n/2) + n
        if r - l == 1:
            return nums[l], nums[l], nums[l]
        m = (l + r) >> 1
        ll, lm, lr = self.divide_conquer(nums, l, m)
        rl, rm, rr = self.divide_conquer(nums, m, r)

        # overall max
        mid = max(lm, rm, lr + rl)
        # max starting from l
        left = max(ll, sum(nums[l: m]) + rl)
        # max ending at r - 1
        right = max(rr, sum(nums[m: r]) + lr)
        return left, mid, right


"""
Time O(NlogN)
Space O(logN)
"""

