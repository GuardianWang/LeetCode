"""
LC 387
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        id_cnt = [[0, 0] for _ in range(26)]
        for i, c in enumerate(s):
            id_cnt[ord(c) - ord('a')][0] = i
            id_cnt[ord(c) - ord('a')][1] += 1
        return min((i for i, cnt in id_cnt if cnt == 1), default=-1)


"""
Time O(N)
Space O(1)
"""

