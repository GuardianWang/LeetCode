"""
LC 763
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
"""
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str):
        ans = []
        # right interval
        c2p = {c: i for i, c in enumerate(s)}
        prev = [0, c2p[s[0]]]
        for l, c in enumerate(s):
            if l <= prev[1]:
                prev[1] = max(prev[1], c2p[c])
            else:
                ans.append(prev[1] - prev[0] + 1)
                prev = [l, c2p[c]]

        ans.append(prev[1] - prev[0] + 1)
        return ans


"""
Time O(N)
Space O(1): 26 letters
"""
        
