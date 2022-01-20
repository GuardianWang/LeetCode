"""
LC 566
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""
from itertools import chain


class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        if r * c != len(mat) * len(mat[0]) or r == len(mat):
            return mat 
        res = [[]]
        for n in chain(*mat):
            res[-1].append(n)
            if len(res[-1]) == c:
                res.append([])
        res.pop()
        return res


"""
Time O(MN)
Space O(MN)
"""

