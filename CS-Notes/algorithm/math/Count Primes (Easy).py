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


def primes(hi):
    def is_prime(n):
        if n <= 3:
            return 1
        if n % 2 == 0 or n % 3 == 0:
            return 0
        bound = int(ceil(sqrt(n)))
        for p in prime_nums:
            if p > bound:
                break
            elif n % p == 0:
                return False
        return True
    prime_nums = []
    for i in range(2, int(hi)):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums


class Solution:
    def countPrimes(self, n: int) -> int:
        return len(primes(n))

