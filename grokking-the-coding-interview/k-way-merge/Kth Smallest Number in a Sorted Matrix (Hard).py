"""
LC 378
Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
Example 1:
Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
"""
from heapq import *


def find_Kth_smallest(matrix, k):
  n = len(matrix)
  t = min(n, k)
  heap = [(matrix[0][col], 0, col) for col in range(t)]
  for _ in range(k):
    val, row, col = heappop(heap)
    # next value
    if row + 1 < n:
      heappush(heap, (matrix[row + 1][col], row + 1, col))

    if t < n:
      heappush(heap, (matrix[0][t], 0, col))
      t += 1
  return val


def main():
  # 2 -5 7 13
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[-5]], 1)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()


"""
T = min(N, K)
Time O(T+KlogT)
Space O(T)
"""
