"""
LC 67
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        to_next = '0'
        for ad, bd in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            digit, to_next = self.add_digit(ad, bd, to_next)
            res.append(digit)
        if to_next == '1':
            res.append('1')
        return "".join(reversed(res))

    def add_digit(self, a, b, to_next):
        # return new_digit new_to_next
        if a == b:
            return to_next, a
        else:
            return '1' if to_next == '0' else '0', to_next 


"""
Time O(N)
Space O(N)
"""

