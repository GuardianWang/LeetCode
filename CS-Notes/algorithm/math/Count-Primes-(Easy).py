"""
LC 204
Given an integer n, return the number of prime numbers that are strictly less than n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""
from math import ceil, sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        elif n == 3:
            return 1

        nums = [1] * n  # 1 for prime
        # mark the multiples of primes
        for i in range(2, int(ceil(sqrt(n))) + 1):
            if nums[i]:  # prime 
                for multi in range(i * i, n, i):
                    # i * k (k < i) has been marked
                    nums[multi] = 0

        return sum(nums) - 2  # exclude 0 and 1

        
"""
\sum 1/p for p < n is loglogn
Time O(N^0.5 loglogN)
Space O(N)
"""

