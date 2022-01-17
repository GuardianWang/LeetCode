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
    prime_nums = []
    for i in range(1, int(hi) + 1):
        if is_prime(i):
            prime_nums.append(i)
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
    return prime_nums


def prime_nums(hi):
    prime_nums_list = primes(hi)
    nums = [0] * int(hi + 1)
    j = 0
    for i in range(len(nums)):
        if j < len(prime_nums_list) and prime_nums_list[j] < i:
            j += 1
        nums[i] = j


class Solution:
    prime_nums_list = prime_nums(5e6)

    def countPrimes(self, n: int) -> int:
        return prime_nums_list[n]

