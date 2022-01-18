"""
LC 169
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums) -> int:
        candidate = nums[0]
        cnt = 0
        for n in nums:
            if cnt == 0:
                candidate = n 

            if n == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate

        
"""
Time O(N)
Space O(1)
"""

