"""
LC 172
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        n2, n5 = 0, 0
        for i in range(1, n + 1):
            res = self.cnt_25(i)
            n2 += res[0]
            n5 += res[1]
        return min(n2, n5)

    def cnt_25(self, n):
        if n < 2:
            return 0, 0
        n2 = 0
        while n > 0 and n % 2 == 0:
            n2 += 1
            n >>= 1 
        n5 = 0
        while n > 0 and n % 5 == 0:
            n5 += 1
            n //=5
        return n2, n5
        

"""
Time O(NlogN):
Space O(1)
"""

