# K-Way Merge

# Problems

1. [Merge K Sorted Lists (medium)](Merge-K-Sorted-Lists-(medium).py)
[[LC23](https://leetcode.com/problems/merge-k-sorted-lists/)]
1. [Kth Smallest Number in M Sorted Lists (Medium)](Kth-Smallest-Number-in-M-Sorted-Lists-(Medium).py)
[[link](https://leetcode.com/discuss/interview-question/727705/google-phone-given-n-sorted-arrays-find-k-smallest-elements)]
1. [Kth Smallest Number in a Sorted Matrix (Hard)](Kth-Smallest-Number-in-a-Sorted-Matrix-(Hard).py)
[[LC378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)]
1. [Smallest Number Range (Hard)](Smallest-Number-Range-(Hard).py)
[[LC632](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)]
1. [K Pairs with Largest Sums (Hard)](K-Pairs-with-Largest-Sums-(Hard).py)
[[LC373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)]

## Pattern

- find the kth value among several sorted list

## Pipeline

```python
from heapq import *


heap = [(x[0], i, 0) for i, x in enumerate(lists)]
for _ in range(k):
  v, i, j = heappop(heap)
  if j + 1 < len(heap[i]):
    heappush(heap, (lists[i][j + 1], i, j + 1))

return v

```

## Types

1. k-th smallest/largest

## Tricks

- divide-conquer in k-way linked list merge
