# Two Heaps

## Problems

1. [Find the Median of a Number Stream (medium)]()
[[LC295](https://leetcode.com/problems/find-median-from-data-stream/)]
1. [Sliding Window Median (hard)]()
[[LC480](https://leetcode.com/problems/sliding-window-median/)]
1. [Maximize Capital (hard)]()
[[LC502](https://leetcode.com/problems/ipo/)]
1. [Next Interval (hard)]()
[[LC436](https://leetcode.com/problems/find-right-interval/)]

## Pattern

- maintain 2 list, only need min/max each time

## Pipeline

### online medium
```python
import heapq
from heapq import *


# because heapq supports min heap, use -n to build max heap
max_heap = []  # smaller half
min_heap = []  # larger half
# maintain
# len(min_heap) == len(max_heap) or
# len(min_heap) == len(max_heap) + 1

def insert(n):
  if not min_heap or min_heap[0] <= n:
    heappush(min_heap, n)
  else:
    heappush(max_heap, -n)

  balance()


def remove(n):
  # find the heap and id to delete
  heap = min_heap if min_heap[0] <= n else max_heap
  i = heap.index(n)
  if i == len(heap) - 1:
    # the last pop last
    heap.pop()
  else:
    # swap i and end, delete end
    heap[i] = heap.pop()
    # sift up and down
    heapq._siftup(heap, i)  # children go up
    heapq._siftdown(heap, 0, i)  # parents go down

  balance()


def medium():
  if len(min_heap) == len(max_heap):
    # even number
    return 0.5 * (min_heap[0] + max_heap[0])
  else:
    # odd
    return min_heap[0]


def balance():
  # before insertion/deletion
  # 1. len(min_heap) == len(max_heap)
  # 2. len(min_heap) == len(max_heap) + 1

  # In 1., insert min_heap or delete max_heap are fine
  # delete min_heap or insert max_heap will lead to
  # len(min_heap) = len(max_heap) - 1

  if len(min_heap) < len(max_heap):
    heappush(min_heap, -heappop(max_heap))

  # In 2., delete min_heap or insert max_heap are fine
  # insert min_heap or delete max_heap will lead to
  # len(min_heap) = len(max_heap) + 2

  if len(min_heap) > len(max_heap) + 1:
    heappush(max_heap, -heappop(min_heap))

```

### conditional two-heap
```python
heap1 = ...
heap2 = ...
while heap1:
  while condition:
    heappop(heap2)
  # or
  if condition:
    heappush(heap2, val)

  if not heap2:
    break
  top1 = heappop(heap1)
  # deal with heap1[0] and heap2[0]
```

## Types

1. median: smaller half and larger half
1. choose the closed based on another: one heap for each

## Tricks

- push tuple to heap to keep track of info e.g., index

## Resources

- [heap deletion](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/heap-delete.html)
- [heapq source code](https://github.com/python/cpython/blob/a09bc3a404befca197b5d9959a9c62110ee61d77/Lib/heapq.py)
