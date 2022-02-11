"""
LC 438
Given a string and a pattern, find all  of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""
from collections import defaultdict

class Solution:
    def findAnagrams(self, str1: str, pattern: str):
        cnt = defaultdict(int)
        for c in pattern:
            cnt[c] += 1
        chars = set(cnt.keys())
        ans = []
        for i, c in enumerate(str1):
            if i >= len(pattern):
                self.add_c(cnt, chars, str1[i - len(pattern)])
            self.rm_c(cnt, chars, c)
            if not cnt:
                ans.append(i - len(pattern) + 1)
        return ans
    
    def add_c(self, cnt, chars, c):
        if c in chars:
            cnt[c] += 1
            if cnt[c] == 0:
                del cnt[c]
                
    def rm_c(self, cnt, chars, c):
        if c in chars:
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]

"""
Time O(N + M)
Space O(N): space to store result
"""

