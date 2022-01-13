# Topological Sort

## Problems

1. [Topological Sort (medium)]()
[[link](https://www.geeksforgeeks.org/topological-sorting/)]
1. [Tasks Scheduling (medium)]()
[[LC207](https://leetcode.com/problems/course-schedule/)]
1. [Tasks Scheduling Order (medium)]()
[[LC210](https://leetcode.com/problems/course-schedule-ii/)]
1. [All Tasks Scheduling Orders (hard)]()
[[LC1916](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/)]
1. [Alien Dictionary (hard)]()
[[LC269](https://leetcode.com/problems/alien-dictionary/)]
1. [Reconstructing a Sequence (hard)]()
[[LC444](https://leetcode.com/problems/sequence-reconstruction/)]
1. [Minimum Height Trees (hard)]()
[[LC310](https://leetcode.com/problems/minimum-height-trees/)]

## Pattern

- prerequisite
- some in-degree order  

## Tricks

- `from collections import defaultdict`
- can also group nodes at the same level
- When calculating combinatorial, can pre-calculate factorial and factorial_inv and use modular inverse.
When p is a prime number, x^(p-1) and 1 mod(p) by Fermat's little theorem, so x^-1 is **x^(p-2)**

## Resources

- [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
- [more problems](https://leetcode.com/tag/topological-sort/)
