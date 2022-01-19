"""
LC 378
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
"""
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        s, l = matrix[0][0], matrix[-1][-1]
        while s < l:
            m = (s + l) >> 1
            cnt, s1, l1 = self.count_le(matrix, m)
            if cnt < k:
                s = l1
            elif cnt > k:
                l = s1
            else:
                return s1
        return s

    def count_le(self, matrix, m):
        # this is O(N)
        cnt = 0
        r, c = len(matrix) - 1, 0
        s, l = matrix[0][0], matrix[-1][-1]
        while r >= 0 and c < len(matrix[0]):
            if m < matrix[r][c]:
                l = min(l, matrix[r][c])
                r -= 1
            else:
                s = max(s, matrix[r][c])
                c += 1
                cnt += r + 1
        return cnt, s, l  # largest number <= m and smallest > m


"""
Time O(Nlog(M-m))
Space O(1)
"""

