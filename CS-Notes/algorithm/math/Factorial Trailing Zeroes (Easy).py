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
        # in factorial, #5 <= #2
        cnt5 = 0
        power_5 = 5
        # count #num with factor 5^k
        while power_5 <= n:
            cnt5 += n // power_5
            power_5 *= 5
        return cnt5


"""
Time log(N)
Space O(1)
"""

