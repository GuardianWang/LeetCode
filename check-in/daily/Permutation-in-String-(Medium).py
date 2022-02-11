"""
LC 567
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        cnt1 = defaultdict(int)
        for c in s1:
            cnt1[c] += 1
        set1 = set(cnt1.keys())

        l = 0
        for r, c in enumerate(s2):
            if c in set1:
                cnt1[c] -= 1
                if 0 == cnt1[c]:
                    del cnt1[c]

            if not cnt1:
                return True

            if r >= len(s1) - 1:
                if s2[l] in set1:
                    cnt1[s2[l]] += 1
                    if 0 == cnt1[s2[l]]:
                        del cnt1[s2[l]]
                l += 1

        return False


"""
Time O(N+M)
Space O(1)
"""
