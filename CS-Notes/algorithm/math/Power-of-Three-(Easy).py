"""
LC 326
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
"""
from math import log 


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3:
                return False
            n //= 3
        return True

    def mathsol(self, n):
        if n <= 0:
            return False 
        l = log(n, 3)
        return abs(round(l) - l) < 1e-11


"""
Time O(logN)
Space O(1)
"""

