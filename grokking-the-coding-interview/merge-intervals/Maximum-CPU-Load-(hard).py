"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).
Example 2:

Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
Example 3:

Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].
"""
from heapq import *


def job(a, b, c):
  return [a, b, c]


def find_max_cpu_load(jobs):
  jobs.sort(key=lambda x: x[0])
  heap = []
  cur, res = 0, 0 
  for job in jobs:
    while heap and heap[0][0] < job[0]:
      cur -= heappop(heap)[1][2]
    heappush(heap, (job[1], job))
    cur += job[2]
    res = max(res, cur)
  return res


def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()


"""
Time O(NlogN)
Space O(N)
"""

