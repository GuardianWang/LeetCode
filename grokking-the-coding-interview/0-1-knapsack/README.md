# 0/1 Knapsack (Dynamic Programming)

## Problems

1. [01 Knapsack (medium)]()
[[link](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)]
1. [Equal Subset Sum Partition (medium)]()
[[LC416](https://leetcode.com/problems/partition-equal-subset-sum/)]
1. [Subset Sum (medium)]()
[[link](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)]
1. [Minimum Subset Sum Difference (hard)]()
[[LC1049](https://leetcode.com/problems/last-stone-weight-ii/
)]
1. [Count of Subset Sum (hard)]()
[[link](https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x/)]
1. [Target Sum (hard)]()
[[LC494](https://leetcode.com/problems/target-sum/)]

## Pattern

- subset sum <= target

## Pipeline

```python
dp = [init] * l
dp[0] = default
for n in nums:
  for i in range(len(dp) - 1, n - 1, -1):
    dp[i] = f(dp[i], dp[i - n])
```

## Types

1. number of subsets
1. existence of subset
1. max weight of subset

## Tricks

- use 1 list and iterate backward to save space

## Resources

- [more dp problems](https://leetcode.com/discuss/study-guide/1308617/Dynamic-Programming-Patterns)
