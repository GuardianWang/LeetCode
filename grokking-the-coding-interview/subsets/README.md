# Subsets

## Problems

1. [Subsets (easy)](Subsets-(easy).py)
[[LC78](https://leetcode.com/problems/subsets/)]
1. [Subsets With Duplicates (easy)](Subsets-With-Duplicates-(easy).py)
[[LC90](https://leetcode.com/problems/subsets-ii/)]
1. [Permutations (medium)](Permutations-(medium).py)
[[LC46](https://leetcode.com/problems/permutations/)]
1. [String Permutations by changing case (medium)](String-Permutations-by-changing-case-(medium).py)
[[LC784](https://leetcode.com/problems/letter-case-permutation/)]
1. [Balanced Parentheses (hard)](Balanced-Parentheses-(hard).py)
[[LC22](https://leetcode.com/problems/generate-parentheses/)]
1. [Unique Generalized Abbreviations (hard)](Unique-Generalized-Abbreviations-(hard).py)
[[LC320](https://leetcode.com/problems/generalized-abbreviation/)]
1. [Evaluate Expression (hard)](Evaluate-Expression-(hard).py)
[[LC241](https://leetcode.com/problems/different-ways-to-add-parentheses/)]
1. [Structurally Unique Binary Search Trees (hard)](Structurally-Unique-Binary-Search-Trees-(hard).py)
[[LC95](https://leetcode.com/problems/unique-binary-search-trees-ii/)]
1. [Count of Structurally Unique Binary Search Trees (hard)](Count-of-Structurally-Unique-Binary-Search-Trees-(hard).py)
[[LC96](https://leetcode.com/problems/unique-binary-search-trees/)]


## Pattern

- solution can be built recursively

## Pipeline

- Find the relationship between f(n) and f(n - 1)
- Build solution by
  1. using all nodes in the tree
  1. using leaves in the tree
  1. using dp and solution to sub-problems

### all nodes
```python
res = [init]
for i in range(n):
  for j in range(len(res)):
    res.append(f(res[j]))
```

### leaves
```python
from collections import deque
res = deque([init])
for i in range(n):
  for j in range(len(res)):
    res.append(f(res.popleft()))
```

### dp
```python
dp[i] = f(dp[0], ..., dp[i - 1])
```

## Types

1. All nodes
1. leaves
1. dp


## Tricks

- the n-th Catalan number is bounded by 4^n / (n sqrt(n))
- C1 = 1, Cn+1 = ((4n + 2) / (n + 2)) Cn
- re.findall(p, s) returns a list
- str.swapcase(), str.upper(), str.lower(), str.isalpha(), str.isdigit()
