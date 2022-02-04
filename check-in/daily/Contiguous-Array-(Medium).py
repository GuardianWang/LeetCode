"""
LC 525
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
class Solution:
    def findMaxLength(self, nums) -> int:
        cnt = 0
        cnt2id = {0: -1}
        ans = 0
        for i, n in enumerate(nums):
            cnt += 1 if n else -1
            if cnt in cnt2id:
            	# array in between has same number of 1 and 0
                ans = max(ans, i - cnt2id[cnt])
            else:
                cnt2id[cnt] = i
        return ans


"""
Time/Space: O(N)
"""
