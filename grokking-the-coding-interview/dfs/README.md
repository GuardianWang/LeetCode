# Depth First Search

## Problems

1. [Binary Tree Path Sum (easy)](Binary-Tree-Path-Sum-(easy).py)
[[LC112](https://leetcode.com/problems/path-sum/)]
1. [All Paths for a Sum (medium)](All-Paths-for-a-Sum-(medium).py)
[[LC113](https://leetcode.com/problems/path-sum-ii/)]
1. [Binary Tree Paths](Binary-Tree-Paths-(easy).py)
[[LC257](https://leetcode.com/problems/binary-tree-paths/)]
1. [Path for Max Sum (medium)](Path-for-Max-Sum-(medium).py)
1. [Sum of Path Numbers (medium)](Sum-of-Path-Numbers-(medium).py)
[[129](https://leetcode.com/problems/sum-root-to-leaf-numbers/)]
1. [Path With Given Sequence (medium)](Path-With-Given-Sequence-(medium).py)
[[LC1430](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/)]
1. [Count Paths for a Sum (medium)](Count-Paths-for-a-Sum-(medium).py)
[[LC437](https://leetcode.com/problems/path-sum-iii/)]
1. [Tree Diameter (medium)](Tree-Diameter-(medium).py)
[[LC543](https://leetcode.com/problems/diameter-of-binary-tree/)]
1. [Path with Maximum Sum (hard)](Path-with-Maximum-Sum-(hard).py)
[[LC124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)]

## Pattern

- tree
- the state of `node` depends on `node.left` and `node.right`

## Pipeline
```python
def dfs(node):
  if node is None:
    return
  # do sth with node.val

  if node.left is None and node.right is None:
    # leaf, base condition
  l = dfs(node.left)
  r = dfs(node.right )
  return # combine l and r
```

## Types

1. path sum
  - root to leaf
  - leaf to leaf
  - subpath, from root to leaf
  - subpath, any

## Tricks

- during the conquer phase, choose best of
  1. each branch
  2. concatenation of each branch and the current node
