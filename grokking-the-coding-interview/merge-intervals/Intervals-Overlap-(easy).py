"""
Given a set of intervals, find out if any two intervals overlap.

Example:

Intervals: [[1,4], [2,5], [7,9]]
Output: true
Explanation: Intervals [1,4] and [2,5] overlap
"""


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

  def __str__(self):
    return "[" + str(self.start) + ", " + str(self.end) + "]"


def find_overlap(intervals):
  intervals.sort(key=lambda x: x.start)
  left = 0
  for it in range(1, len(intervals)):
    if intervals[it].start <= intervals[left].end:
      return True
    else:
      left = it
  return False


def main():
  print(find_overlap([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
  print(find_overlap([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))
  print(find_overlap([Interval(1, 4), Interval(2, 6), Interval(3, 5)]))


main()

    
"""
Time O(NlogN)
Space O(N): sorting
"""

