"""
LC 1198
https://hjweds.gitbooks.io/leetcode/content/common-elements-in-three-sorted-array.html

Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Example 2:

Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for n in mat[0]:
            for row in islice(mat, 1, len(mat)):
                idx = bisect_left(row, n)
                if idx == len(row):  # this value is too large
                    return res or -1 
                if row[idx] != n:
                    break
            else:
                return n
        return -1


"""
Time O(NMlogM)
Space O(1)
"""
