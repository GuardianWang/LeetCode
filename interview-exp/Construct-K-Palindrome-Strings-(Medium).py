"""
LC 1400
https://leetcode.com/playground/Pi77u5Sr k = 1
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
"""
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        cnt = Counter(s)
        # at most k odd frequency
        n_odd_freq = sum(freq & 1 for freq in cnt.values())
        return n_odd_freq <= k
        

"""
Time O(N)
Space O(1)
"""        
