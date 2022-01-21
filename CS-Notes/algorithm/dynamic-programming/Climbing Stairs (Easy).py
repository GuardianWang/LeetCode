"""
LC 70
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        q = [[1, 1], [1, 0]]  # q^n[0][0] is answer
        return self.qpow(q, n)[0][0]

    def qpow(self, q, n):
        # binary n is 1 1 0 0 1
        # q^n = q^(0 0 0 0 1) * q^(0 1 0 0 0) * q^(1 0 0 0 0)
        power = 1
        remain = [[1, 0], [0, 1]]
        while power <= n:
            if n & power:
                remain = self.qmul(remain, q)
            q = self.qmul(q, q)
            power <<=1
        return remain

    def qmul(self, a, b):
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], 
                 a[0][0] * b[0][1] + a[0][1] * b[1][1]], 
                [a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]]]


"""
Time O(logN)
Space O(1)
"""

