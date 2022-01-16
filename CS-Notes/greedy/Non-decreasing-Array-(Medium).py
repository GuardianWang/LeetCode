"""
LC 665
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""
class Solution:
    def checkPossibility(self, nums) -> bool:
        # if nums[i] > nums[i + 1], modify nums[i] or nums[i + 1]
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if cnt == 1:
                    return False

                if self.can_modify(nums, i):
                    cnt += 1
                else:
                    return False 
        return True

    def can_modify(self, nums, i):
        left_ok = True 
        if i >= 1:
            left_ok = nums[i - 1] <= nums[i + 1]
        if left_ok:
            return True

        right_ok = True 
        if i + 2 < len(nums):
            right_ok = nums[i] <= nums[i + 2]
        return right_ok


"""
Time O(N)
Space O(1)
"""

