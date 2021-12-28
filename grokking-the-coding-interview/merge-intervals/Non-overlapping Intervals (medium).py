"""
Given a list of appointments, find all the conflicting appointments.

Example:

Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
"""


def find_conflicts(intervals):
  intervals.sort(key=lambda x: x[0])
  left = 0
  for l in range(len(intervals) - 1):
    for i in range(l + 1, len(intervals)):
      if intervals[i][0] < intervals[l][1]:
        print(intervals[l], intervals[i])
      else:
        break


find_conflicts([[4,5], [2,3], [3,6], [5,7], [7,8]])


"""
Time O(N^2)
Space O(N^2)
"""

