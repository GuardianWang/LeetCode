"""
LC 973
Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
Example 1:
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:
Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""
from heapq import *


def find_closest_points(points, k):
  h = []  # max heap
  for p in points:
    d_square = d2(p)
    if len(h) < k:
      heappush(h, (-d_square, p))
    elif d_square < -h[0][0]:
      heapreplace(h, (-d_square, p))
  return [x[1] for x in h]


def d2(p):
  return p[0] ** 2 + p[1] ** 2


"""
Time O(NlogK)
Space O(K)
"""

