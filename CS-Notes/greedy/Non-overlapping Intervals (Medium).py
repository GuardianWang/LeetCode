"""
LC 435
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        prev = 0
        cnt = 0
        for cur in range(1, len(intervals)):
            if intervals[cur][0] < intervals[prev][1]:
                cnt += 1
                if intervals[cur][1] < intervals[prev][1]:
                    prev = cur  # keep smaller interval 
                    # else, keep lefter interval
            else:
                prev = cur 
        return cnt


"""
Time O(NlogN)
Space O(N): sort
"""

