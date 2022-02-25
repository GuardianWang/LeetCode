"""
LC 1621
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
"""
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # k interval lengths: x_i >= 1
        # k + 1 spaces: s_i >= 0
        # d_i = x_i - 1 >= 0
        # 2k + 1 vars: d_i and s_i
        
        # sum(x_i + s_i) = n - 1  # n - 1 gaps
        # sum(d_i + s_i) = n - k - 1
        
        # (n - k - 1) + (2k + 1) - 1 choose (2k + 1) - 1
        
        return comb(n + k - 1, 2 * k) % int(1e9 + 7)
        

"""
Time O(n - k)
Space O(1)
"""        
