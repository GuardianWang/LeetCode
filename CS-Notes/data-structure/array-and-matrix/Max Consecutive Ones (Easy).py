"""
LC 485
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        l = 0
        ans = 0
        for r, n in enumerate(nums):
            if n:
                ans = max(ans, r - l + 1)
            else:
                l = r + 1
        return ans
        

"""
Time O(N)
Space O(1)
"""

