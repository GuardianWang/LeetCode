"""
LC 790
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
"""
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        MOD = int(1e9 + 7)
        # f(n) = f(n - 1) + f(n - 2) + 2 * p(n - 1)
        f = (1, 1)  # full
        # p(n) = p(n - 1) + f(n - 2)
        p = (0, 0)  # partial, upper right is vacant
        
        for _ in range(n - 1):
            f, p = (f[1], (f[0] + f[1] + 2 * p[1]) % MOD), (p[1], (p[1] + f[0]) % MOD)
            # print(f, p)
        return f[-1]


"""
Time O(N)
Space O(1)
"""
