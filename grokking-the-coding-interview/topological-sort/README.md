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

## Pipeline

### in-degree and adjacency matrix
```python
from collections import defaultdict


node2children = defaultdict(list)
node2in_deg = defaultdict(int)
for from_node, to_node in edges:
  node2children[from_node].append(to_node)
  node2in_deg[from_node] += 1
```

### normal
```python
# source in-deg == 0
order = [node for node in nodes if node not in node2in_deg]
ptr = 0
while ptr < len(order):
  next_ptr = len(order)
  for i in range(ptr, next_ptr):
    for child in node2children[order[i]]:
      node2in_deg[child] -= 1
      if node2in_deg[child] == 0:
        order.append(child)
  ptr = next_ptr

return order
```

### group
Vertices in the same sub-group can change the relative order.
The most front position should be after its last parent.
```python
# source in-deg == 0
order = [[node for node in nodes if node not in node2in_deg]]
while order[-1]:
  subgroup = []
  for node in order[-1]:
    for child in node2children[node]:
      node2in_deg[child] -= 1
      if node2in_deg[child] == 0:
        subgroup.append(child)
  order.append(subgroup)
order.pop()
```

## Types

1. topological sort order: add v one by one
1. #order of a tree: add v by group

## Tricks

- `from collections import defaultdict`
- can also group nodes at the same level
- When calculating combinatorial, can pre-calculate factorial and factorial_inv and use modular inverse.
When p is a prime number, x^(p-1) and 1 mod(p) by Fermat's little theorem, so x^-1 is **x^(p-2)**
- set add remove are O(1)

## Resources

- [Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
- [more problems](https://leetcode.com/tag/topological-sort/)
