# Top K Elements

## Problems

1. [Top 'K' Numbers (easy)](Top-'K'-Numbers-(easy).py)
1. [Kth Smallest Number (easy)](Kth-Smallest-Number-(easy).py)
[[LC215](https://leetcode.com/problems/kth-largest-element-in-an-array/)]
1. ['K' Closest Points to the Origin (easy)]('K'-Closest-Points-to-the-Origin-(easy).py)
[[LC973](https://leetcode.com/problems/k-closest-points-to-origin/)]
1. [Connect Ropes (easy)](Connect-Ropes-(easy).py)
[[LC1167](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)]
1. [Top 'K' Frequent Numbers (medium)](Top-'K'-Frequent-Numbers-(medium).py)
[[LC347](https://leetcode.com/problems/top-k-frequent-elements/)]
1. [Frequency Sort (medium)](Frequency-Sort-(medium).py)
[[LC451](https://leetcode.com/problems/sort-characters-by-frequency/)]
1. [Kth Largest Number in a Stream (medium)](Kth-Largest-Number-in-a-Stream-(medium).py)
[[LC703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)]
1. ['K' Closest Numbers (medium)]('K'-Closest-Numbers-(medium).py)
[[LC658](https://leetcode.com/problems/find-k-closest-elements/)]
1. [Maximum Distinct Elements (medium)](Maximum-Distinct-Elements-(medium).py)
[[LC1481](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)]
1. [Sum of Elements (medium)](Sum-of-Elements-(medium).py)
[[link](https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/)]
1. [Rearrange String (hard)](Rearrange-String-(hard).py)
[[LC767](https://leetcode.com/problems/reorganize-string/)]
1. [Rearrange String K Distance Apart (hard)](Rearrange-String-K-Distance-Apart-(hard).py)
[[LC358](https://leetcode.com/problems/rearrange-string-k-distance-apart/)]
1. [Scheduling Tasks (hard)](Scheduling-Tasks-(hard).py)
[[LC621](https://leetcode.com/problems/task-scheduler/)]
1. [Frequency Stack (hard)](Frequency-Stack-(hard).py)
[[LC895](https://leetcode.com/problems/maximum-frequency-stack/)]

## Pattern

- max/min k values

## Pipeline

- maintain a min heap for max k values or 
maintain a max heap for min k values

## Types

1. top k values
1. arrange letters: also maintain a deque of letters to be pushed to heap

## Tricks

- quickselect/partition
- to sort by **frequency**, use bucket sort to have O(N) time 
- count with [collections.defaultdict(int)](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) Note: this is sorted, so O(NlogN) time by default
- push a tuple to the heap to sort by multiple keys
