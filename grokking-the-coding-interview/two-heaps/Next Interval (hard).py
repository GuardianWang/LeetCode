"""
LC 436
Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval i its next interval j will have the smallest ‘start’ greater than or equal to the ‘end’ of i.

Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

Example 1:

Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6] having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

Example 2:

Input: Intervals [[3,4], [1,5], [4,6]]
Output: [2, -1, -1]
Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].
"""
from heapq import *


def Interval(a, b):
    return [a, b]


def find_next_interval(intervals):
    min_start_heap = [(x[0], i) for i, x in enumerate(intervals)]
    min_end_heap = [(x[1], i) for i, x in enumerate(intervals)]
    heapify(min_start_heap)
    heapify(min_end_heap)

    res = [-1] * len(intervals)
    while min_end_heap:
        while min_start_heap and min_end_heap[0][0] > min_start_heap[0][0]:
            heappop(min_start_heap)
        if not min_start_heap:
            break
        res[heappop(min_end_heap)[1]] = min_start_heap[0][1]
    return res 

def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()


"""
Time O(NlogN)
Space O(N)
"""

