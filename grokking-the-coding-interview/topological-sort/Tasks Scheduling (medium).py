"""
LC 207
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2] 
Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scHeduling of tasks is: [0 1 4 3 2 5]
"""
from collections import defaultdict


def is_scheduling_possible(tasks, prerequisites):
    node2children, node2in_deg = build_map(prerequisites)
    # sources
    schedule = [task for task in range(tasks) if task not in node2in_deg]
    ptr = 0
    while ptr < len(schedule):
        next_ptr = len(schedule)
        for i in range(ptr, next_ptr):
            node = schedule[i]
            for child in node2children[node]:
                node2in_deg[child] -= 1
                if node2in_deg[child] == 0:
                    schedule.append(child)
        ptr = next_ptr

    return len(schedule) == tasks


def build_map(prerequisites):
    node2children = defaultdict(list)
    node2in_deg = defaultdict(int)
    for from_node, to_node in prerequisites:
        node2children[from_node].append(to_node)
        node2in_deg[to_node] += 1
    return node2children, node2in_deg


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()


"""
Time/Space O(V+E)
"""

