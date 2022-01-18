"""
LC 594
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
"""
from collections import defaultdict


class Solution:
    def findLHS(self, nums) -> int:
        counter = defaultdict(int)
        res = 0
        for n in nums:
            counter[n] += 1
            if n + 1 in counter:
                res = max(res, counter[n] + counter[n + 1])
            if n - 1 in counter:
                res = max(res, counter[n] + counter[n - 1])

        return res


"""
Time/Space O(N)
"""

