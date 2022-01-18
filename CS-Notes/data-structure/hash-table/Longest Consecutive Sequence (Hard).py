"""
LC 128
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        res = 0
        while nums:
            n = nums.pop()
            cnt = 1
            num = n + 1
            while num in nums:
                nums.remove(num)
                cnt += 1
                num += 1 
            num = n - 1 
            while num in nums:
                nums.remove(num)
                cnt += 1
                num -= 1 
            res = max(res, cnt)

        return res


"""
Time/Space O(N)
"""
        
