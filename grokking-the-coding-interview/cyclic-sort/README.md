# Cyclic Sort

# Problems

1. [Cyclic Sort (easy)]()
1. [Find the Missing Number (easy)]()
[[LC268](https://leetcode.com/problems/missing-number/)]
1. [Find all Missing Numbers (easy)]()
[[LC448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)]
1. [Find the Duplicate Number (easy)]()
1. [Find all Duplicate Numbers (easy)]()
[[LC442](https://leetcode.com/problems/find-all-duplicates-in-an-array/)]
1. [Find the Corrupt Pair (easy)]()
[[link](https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/)]
1. [Find the Smallest Missing Positive Number (medium)]()
[[LC41](https://leetcode.com/problems/first-missing-positive/submissions/)]
1. [Find the First K Missing Positive Numbers (hard)]()

## Pattern

- unsorted integer array
- find duplicated/missing values

## Pipeline

### cyclic sort
```python
# if value i + 1 occurs, put it at index i
for i, n in enumerate(nums):
	j = nums[i] - 1  # next index, suppose value i is in [1, n] and i is placed at nums[i - 1]
	while n != nums[j] and ignore_value(n):  # E.g., ignore n s.t. n is out of index range
		# stop when either
		# 1. don't move: j = nums[j] - 1, i.e. n - 1 = nums[j] - 1, or
		# 2. duplicate: n = nums[j]
		# Therefore, we can use n= nums[j] to cover both cases.
		swap(nums, i, j)
		# update n and j
for i, n in enumerate(nums):
	if i != n - 1: 
		# not on the right place
		# value i + 1 is missing 
		# value n is a duplicate
```

### new_value = k * M + old_value
```python
# old_value = new_value % M
# appear time = new_value // M

# make sure M > max(nums)
M = max(nums) + 1  # usually len(nums) + 1
for i, n in enumerate(nums):
	nums[n % M - 1] += M 
for i, n in enumerate(nums):
	if n > 2 * M:
		# value i + 1 is a duplicate
	elif n < M:
		# value i + 1 is missing
```

Cons:
- applicable only when 0 <= nums[i] <= len(nums), otherwise, need to reset other values

## Types

1. find duplicates
2. find missing values

## Tricks

- only 1 missing: XOR
- value out of index range: ignore
