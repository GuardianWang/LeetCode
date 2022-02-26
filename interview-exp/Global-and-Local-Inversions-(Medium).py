"""
LC 775
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:

0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.

 

Example 1:

Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.
Example 2:

Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.
"""
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        running_min = nums[-1]
        # check value pairs whose indices have difference of 2
        for i in range(len(nums) - 1, 1, -1):
            running_min = min(nums[i], running_min)
            if nums[i - 2] > running_min:
                return False
        return True


"""
Time O(N)
Space O(1)
"""
