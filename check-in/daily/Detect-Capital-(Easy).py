"""
LC 520
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
"""
class Solution:
    def detectCapitalUse(self, s: str) -> bool:
        lower_cnt, upper_cnt = 0, 0
        for c in s:
            if c.islower():
                lower_cnt += 1
            else:
                upper_cnt += 1
        return lower_cnt == len(s) or upper_cnt == len(s) or (upper_cnt == 1 and s[0].isupper())


"""
Time O(N)
Space O(1)
"""

