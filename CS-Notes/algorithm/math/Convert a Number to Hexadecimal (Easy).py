"""
LC 405
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
"""
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            # 2's component
            num += (1 << 32)
        base = 16
        n2c = {x: str(x) for x in range(10)}
        n2c.update({x: chr(ord('a') + x - 10) for x in range(10, base)})
        res = []
        while num:
            res.append(n2c[num % base])
            num //= base 
        return "".join(reversed(res))


"""
Time/Space O(logN)
"""

