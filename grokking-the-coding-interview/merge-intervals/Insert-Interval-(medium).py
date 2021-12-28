"""
LC 57
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


def insert(intervals, new_interval):
    res = []
    l, r = 0, 1
    for i, interval in enumerate(intervals):
      if interval[r] < new_interval[l]:
        res.append(interval)
      elif new_interval[r] < interval[l]:
        res.append(new_interval)
        res.extend(intervals[i:])
        break
      else:
        new_interval[l] = min(new_interval[l], interval[l])
        new_interval[r] = max(new_interval[r], interval[r])
    else:  # end of for loop
      res.append(new_interval)
    return res


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()


"""
Time O(N)
Space O(N)
"""

