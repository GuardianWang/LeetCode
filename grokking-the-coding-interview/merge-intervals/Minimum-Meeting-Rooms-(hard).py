"""
LC 253
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.

Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
"""
import heapq


def Meeting(a, b):
  return [a, b]


def min_meeting_rooms(meetings):
  meetings.sort(key=lambda x: x[0])
  heap = []
  res = 0
  for m in meetings:
    while heap and heap[0] <= m[0]:
      # remove the meetings that are done
      heapq.heappop(heap)
    heapq.heappush(heap, m[1])
    res = max(res, len(heap))
  return res 


def main():
  # 2 2 1 2 2 1 3 1
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))) 
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(1,2), Meeting(2, 3), Meeting(3, 4), Meeting(4, 5)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(1, 5), Meeting(2, 3), Meeting(3, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5)])))


main()


"""
Time O(NlogN)
Space O(N)
"""

