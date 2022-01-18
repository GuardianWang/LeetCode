"""
LC 283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the first 0
        l = self.next0(nums, 0)
        # the next non-0
        r = self.next_non0(nums, l)
        # swap 0 and number
        for r in range(r, len(nums)):
            if nums[r]:
                self.swap(nums, l, r)
                # next 0
                l = self.next0(nums, l)
            
    def next0(self, nums, start):
        while start < len(nums):
            if nums[start] == 0:
                break
            start += 1
        return start

    def next_non0(self, nums, start):
        while start < len(nums):
            if nums[start]:
                break
            start += 1
        return start

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
        

"""
Time O(N): #non-0 after the first 0
Space O(1)
"""

