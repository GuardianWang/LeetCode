"""
Given a list of intervals representing the arrival and departure times of trains to a train station, our goal is to find the minimum number of platforms required for the train station so that no train has to wait.
"""
from heapq import *


def findPlatform(intervals):
  heap = []
  intervals.sort(key=lambda x: x[0])
  res = 0
  for interval in intervals:
    while heap and heap[0] < interval[0]:
      heappop(heap)
    heappush(heap, interval[1])
    res = max(res, len(heap))
  return res 


print(findPlatform([[900, 910], [940, 1200], [950, 1120], [1100, 1130], [1500, 1900], [1800, 2000]]))  # 3


"""
Time O(NlogN)
Space O(N)
"""

