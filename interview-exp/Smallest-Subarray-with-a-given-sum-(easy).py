"""
LC 209
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        smallest_len = len(nums) + 1
        
        for r, n in enumerate(nums):
            s += n
            while s >= target:
                smallest_len = min(smallest_len, r - l + 1)
                s -= nums[l]
                l += 1
                
        return smallest_len if smallest_len <= len(nums) else 0
            

"""
Time O(N)
Space O(1)
"""
