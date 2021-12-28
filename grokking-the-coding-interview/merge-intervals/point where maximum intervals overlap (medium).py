"""
Given a list of intervals, find the point where the maximum number of intervals overlap.
"""
from heapq import *


def findMaxGuests(intervals):
  intervals.sort(key=lambda x: x[0])
  heap = []
  max_len, p = 0, 0
  for interval in intervals:
    while heap and interval[0] > heap[0]:
      heappop(heap)
    heappush(heap, interval[1])
    if len(heap) > max_len:
      max_len = len(heap)
      p = interval[0]
  return p


print(findMaxGuests([[1, 4], [2, 5], [10, 12], [5, 9], [5, 12]]))  # 5


"""
Time O(NlogN)
Space O(N)
"""

