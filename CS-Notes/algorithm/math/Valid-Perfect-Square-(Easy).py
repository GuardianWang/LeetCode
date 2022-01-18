"""
LC 367
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.int_sqrt(num) ** 2 == num

    def int_sqrt(self, num):
        l, r = 0, num 
        while l < r:
            m = r - ((r - l) >> 1)
            m2 = m * m
            if m2 <= num:
                l = m
            else:
                r = m - 1
        return l


"""
Time O(logN)
Space O(1)
"""

