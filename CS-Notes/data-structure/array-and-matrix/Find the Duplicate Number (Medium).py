"""
LC 287
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
"""
class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = 0, nums[0]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        cnt = 1
        slow = nums[slow]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            cnt += 1
        slow, fast = 0, 0
        for _ in range(cnt):
            fast = nums[fast]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]


"""
Time O(N)
Space O(1)
"""
