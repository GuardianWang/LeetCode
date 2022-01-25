"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
"""
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Within a non-increasing suffix, we cannot just rearrange values
        # because decreasing subarray is the largest permutation with all those numbers.
        # To find the next permutation, just increase the number before non-increasing suffix.
        p = self.find_start_of_decreasing_suffix(nums)
        if p > 0:
            larger_id = self.find_greater(nums, p, len(nums) - 1, nums[p - 1])
            self.swap(nums, p - 1, larger_id)
            # After swap, nums[p:] is still non-increasing
        self.reverse(nums, p, len(nums) - 1)

        
    def find_greater(self, nums, l, r, n):
        for i in range(r, l - 1, -1):
            if nums[i] > n:
                return i

    def find_start_of_decreasing_suffix(self, nums):
        p = len(nums) - 1
        while p >= 1 and nums[p - 1] >= nums[p]:
            p -= 1
        return p

    def reverse(self, nums, l, r):
        while l < r:
            self.swap(nums, l, r)
            l += 1
            r -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


"""
Time O(N)
Space O(1)
"""
