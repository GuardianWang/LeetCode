"""
LC 504
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        base = 7
        sign = ""
        if num < 0:
            sign = '-'
            num = -num
        res = []
        while num >= base:
            res.append(str(num % 7))
            num = num // 7
        res.append(str(num))
        res.append(sign)
        return "".join(reversed(res))


"""
Time/Space log(N)
"""

