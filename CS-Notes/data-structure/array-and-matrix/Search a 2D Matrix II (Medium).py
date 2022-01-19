"""
LC 240
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            col = self.search_row(matrix, target, row, 0, col)
            if matrix[row][col] == target:
                return True
            row += 1

            if row >= len(matrix):
                return False

            row = self.search_col(matrix, target, col, row, len(matrix) - 1)
            if matrix[row][col] == target:
                return True
            col -= 1
        return False

    def search_row(self, matrix, target, row, l, r):
        # row binary search
        while l < r:
            m = l + ((r - l) >> 1)
            if matrix[row][m] < target:
                l = m + 1
            else:
                r = m
        return l  # vec[l] >= target

    def search_col(self, matrix, target, col, l, r):
        # col 
        while l < r:
            m = r - ((r - l) >> 1)
            if matrix[m][col] <= target:
                l = m
            else:
                r = m - 1
        return l  # vec[l] <= target


"""
Time O(NlogM+MlogN)
Space O(1)
"""

