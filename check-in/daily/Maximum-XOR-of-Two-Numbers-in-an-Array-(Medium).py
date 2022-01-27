"""
LC 421
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
"""
class Solution:
    def findMaximumXOR(self, nums) -> int:
        if len(nums) == 1:
            return 0
        n_bits = max(len(bin(n)) for n in nums) - 2
        max_or = 0
        for i in reversed(range(n_bits)):
            # try possible max_or prefixes
            max_or <<= 1
            cur_or = max_or | 1  # +1
            prefixes = {n >> i for n in nums}
            # similar to two-sum, this is two-xor
            if any(cur_or ^ p in prefixes for p in prefixes):
                max_or = cur_or
        return max_or
            

"""
Time/Space O(N)
"""

