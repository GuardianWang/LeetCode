# Merge Intervals

## Problems

1. [Merge Intervals (medium)](Merge-Intervals-(medium).py)
[[LC56](https://leetcode.com/problems/merge-intervals/)]
1. [Intervals Overlap (easy)](Intervals-Overlap-(easy).py)
1. [**Insert Interval (medium)**](Insert-Interval-(medium).py)
[[LC57](https://leetcode.com/problems/insert-interval/)]
1. [Intervals Intersection (medium)](Intervals-Intersection-(medium).py)
[[LC986](https://leetcode.com/problems/interval-list-intersections/)]
1. [Conflicting Appointments (medium)](Conflicting-Appointments-(medium).py)
1. [Non-overlapping Intervals](Non-overlapping-Intervals-(medium).py)
1. [Minimum Meeting Rooms (hard)](Minimum-Meeting-Rooms-(hard).py)
[[LC253](https://leetcode.com/problems/meeting-rooms-ii/)]
1. [point where maximum intervals overlap](point-where-maximum-intervals-overlap-(medium).py)
[[link](https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/)]
1. [minimum number of platforms](minimum-number-of-platforms-(medium).py)
[[link](https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/)]
1. [Maximum CPU Load (hard)](Maximum-CPU-Load-(hard).py)
[[link](https://www.geeksforgeeks.org/maximum-cpu-load-from-the-given-list-of-jobs/)]
1. [Employee Free Time (hard)](Employee-Free-Time-(hard).py)
[[LC759](https://leetcode.com/problems/employee-free-time/)]

## Pattern

- intervals

## Pipeline

```python
# merge
intervals.sort(key=lambda x: x.start)
for interval in intervals:
	if interval.start <= last_interval:
		previous_interval.end = max(previous_interval.end, interval.end)
	else:
		previous_interval = interval


# intersection
from heapq import *
intervals.sort(key=lambda x: x.start)
heap = []  # contains interval.end
for interval in intervals:
	heappush(heap, interval.end)
	while heap[0] < interval.start:
		heappop(heap)
	# heap contains overlapped intervals
	# intersection is [interval.start, heap[0]]


def union(in1, in2):
	new.start = min(in1.start, in2.start)
	new.end = max(in1.end, in2.end)


def intersect(in1, in2):
	new.start = max(in1.start, in2.start)
	new.end = min(in1.end, in2.end)
```

## Types

1. merge intervals: sort and compare previous.end and current.start
2. intersection: maintain a min heap by interval.end

## Tricks

- overlap: i2.start <= i1.start <= i2.end or i1.start <= i2.start <= i1.end
- In the question, does i1.start == i2.end indicate overlap?
- when don't need to save all merged intervals, only keep track of the last seen one
- subsets are sorted: k-way merge sort by priority queue
- to save objects in heapq, use tuple: heappush(heap, (key, object))
- if key of heap is not unique, use some unique id as the other element to prevent comparision of incomparable objects
- if want i to be len(arr) after a loop, use while loop instead of for loop: `while i < len(arr): i += 1`
