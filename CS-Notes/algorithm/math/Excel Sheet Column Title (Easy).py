"""
LC 168
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
"""
# https://leetcode.com/problems/excel-sheet-column-title/discuss/441430/Detailed-Explanation-Here's-why-we-need-n-at-first-of-every-loop-(JavaPythonC%2B%2B)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        base = 26
        while columnNumber:
            # get the correct remainder
            columnNumber -= 1
            res.append(chrs[columnNumber % base])
            columnNumber //= base 
        return "".join(reversed(res))


"""
Time/Space O(logN)
"""

