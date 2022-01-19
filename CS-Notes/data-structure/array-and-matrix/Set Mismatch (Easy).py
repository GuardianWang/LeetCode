"""
LC 645
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
"""
class Solution:
    def findErrorNums(self, nums):
        M = len(nums) + 1
        for n in nums:
            nums[n % M - 1] += M
        res = [0, 0]
        M2 = 2 * M
        for i, n in enumerate(nums):
            if n < M:
                res[1] = i + 1  # missing
            elif n > M2:
                res[0] = i + 1  # duplicate
        return res


"""
Time O(N)
Space O(1)
"""

