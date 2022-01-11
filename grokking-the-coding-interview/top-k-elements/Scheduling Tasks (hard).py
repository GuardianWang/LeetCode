"""
LC 621
You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.
If at any time the server can’t execute any task then it must stay idle.
Example 1:
Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a
Example 2:
Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
"""
from collections import deque
from heapq import *


def schedule_tasks(tasks, k):
  if len(tasks) <= 1:
    return len(tasks)
  if k == 0:
    return len(tasks)

  # count
  freqs = {}
  for task in tasks:
    if task in freqs:
      freqs[task] += 1
    else:
      freqs[task] = 1
  freqs = list(freqs.values())
  max_f = max(freqs)
  n_max = freqs.count(max_f)
  # only consider the most frequent tasks
  # if gaps are needed, gaps happend for 1 of the most frequent tasks
  # the tail has n_max tasks 
  # the front has max_f - 1 groups, k + 1 values in each

  return max(len(tasks), n_max + (k + 1) * (max_f - 1))


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()


"""
#letters is O(1)
Time O(N)
Space O(1)
"""
