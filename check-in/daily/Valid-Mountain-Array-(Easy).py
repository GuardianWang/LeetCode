"""
LC 941
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""
class Solution:
    def validMountainArray(self, arr) -> bool:
        l, r = 0, len(arr) - 1
        while l + 1 < len(arr) and arr[l + 1] > arr[l]:
            l += 1
        while r >= 1and arr[r - 1] > arr[r]:
            r -= 1
        return l == r and 0 < l < len(arr) - 1


"""
Time O(N)
Space O(1)
"""

