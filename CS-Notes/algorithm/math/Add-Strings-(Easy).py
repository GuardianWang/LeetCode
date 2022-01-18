"""
LC 415
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2))
        if len(num1) < l:
            num1 = num1.zfill(l)
        if len(num2) < l:
            num2 = num2.zfill(l)
        to_next = '0'
        res = []
        for c1, c2 in zip(reversed(num1), reversed(num2)):
            digit, to_next = self.cal_digit(c1, c2, to_next)
            res.append(digit)
        if to_next != '0':
            res.append(to_next)
        return "".join(reversed(res))

    def cal_digit(self, n1, n2, to_next):
        # return new_digit, new_to_next
        n1, n2, to_next = int(n1), int(n2), int(to_next)
        s = n1 + n2 + to_next
        return str(s % 10), str(s // 10)


"""
Time/Space O(N)
"""

