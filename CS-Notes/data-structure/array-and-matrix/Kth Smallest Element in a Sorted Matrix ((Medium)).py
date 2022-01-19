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
from heapq import *


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        h = [[matrix[i][0], i, 1] for i in range(min(k, len(matrix)))]  # min heap 
        next_row = h[-1][1] + 1
        for _ in range(k):
            m, row, col = heappop(h)
            if col < len(matrix[0]):
                heappush(h, [matrix[row][col], row, col + 1])
            if next_row < len(matrix):
                heappush(h, [matrix[next_row][0], next_row, 0])
                next_row += 1
        return m


"""
Time O(T+KlogT) T=min(N,K)
Space O(T)
"""

