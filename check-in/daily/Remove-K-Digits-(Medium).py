"""
LC 402
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        # maintain order: stack
        
        res = []  # non-decreasing
        for n in num:
            while k and res and res[-1] > n:
                res.pop()
                k -= 1
            res.append(n)
        if k > 0:
            # remove k
            res = res[:-k]
        
        return "".join(res).lstrip('0') or '0'
    

"""
Time/Space O(N)
"""
