"""
LC 766
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""
class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        r, c = len(matrix) - 1, 0
        while r >= 0:
            if not self.isT(matrix, r, c):
                return False 
            r -= 1
        r = 0
        while c < len(matrix[0]):
            if not self.isT(matrix, r, c):
                return False 
            c += 1
        return True

    def isT(self, matrix, r, c):
        base = matrix[r][c]
        while r < len(matrix) and c < len(matrix[0]):
            if matrix[r][c] != base:
                return False 
            r += 1
            c += 1
        return True 


"""
Time O(N)
Space O(1)
"""

