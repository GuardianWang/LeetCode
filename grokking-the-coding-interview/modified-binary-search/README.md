# Modified Binary Search

## Problems

1. [Order-agnostic Binary Search (easy)](Order-agnostic-Binary-Search-(easy).py)
[[LC704](https://leetcode.com/problems/binary-search/)]
1. [Ceiling of a Number (medium)](Ceiling-of-a-Number-(medium).py)
[[LC35](https://leetcode.com/problems/search-insert-position/)]
1. [Floor of a Number (medium)](Floor-of-a-Number-(medium).py)
[[link](https://www.geeksforgeeks.org/floor-in-a-sorted-array/)]
1. [Next Letter (medium)](Next-Letter-(medium).py)
[[LC744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)]
1. [Number Range (medium)](Number-Range-(medium).py)
[[LC34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)]
1. [Search in a Sorted Infinite Array (medium)](Search-in-a-Sorted-Infinite-Array-(medium).py)
[[LC702](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)]
1. [Minimum Difference Element (medium)](Minimum-Difference-Element-(medium).py)
[[LC658](https://leetcode.com/problems/find-k-closest-elements/)]
1. [Bitonic Array Maximum (easy)](Bitonic-Array-Maximum-(easy).py)
[[LC852](https://leetcode.com/problems/peak-index-in-a-mountain-array/)]
1. [Search Bitonic Array (medium)](Search-Bitonic-Array-(medium).py)
[[LC1095](https://leetcode.com/problems/find-in-mountain-array/)]
1. [Search in Rotated Array (medium)](Search-in-Rotated-Array-(medium).py)
[[LC33](https://leetcode.com/problems/search-in-rotated-sorted-array/)]
1. [Search in Rotated Sorted Array II](Search-in-Rotated-Sorted-Array-II.py)
[[LC81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)]
1. [Rotation Count (medium)](Rotation-Count-(medium).py)
[[LC153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)]
1. [Rotation Count II (medium)](Rotation-Count-II-(medium).py)
[[LC154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)]

## Pattern

- find value in sorted array

## Pipeline

### l <= r
Need to consider two things:
1. which branch does equal condition go to
1. return l or r

First consider returning l or r:

The last iteration will be l == r, and don't consider equal,
e.g., key < arr[m], if need to return m, then use l (r will -1 but l remains the same).
Otherwise, return r.

Then consider which branch does equal condition go to:

Still consider l == r and consider equal,
e.g., key == arr[m]. Suppose we have decided to return l, then we change r (keep l the same as m),
so equal condition goes to the r = m - 1 branch.

Cons:
1. may go out of index range (first consider edge conditions)

```python
l, r = 0, len(arr) - 1
while l <= r:
  m = l + (r - l >> 1)
  if in_left_half_condition:
    r = m - 1
  else:
    l = m + 1
```

### l < r
Need to consider two things:
1. which branch does equal condition go to
1. m = l + (r - l >> 1) or r - (r - l >> 1)

First consider how to calculate m:

Similarly, first consider l = r - 1 and don't consider equal,
e.g., key < arr[m]. Suppose we have decided to return m, then we want
m = l + (r - l >> 1) because r = m will become l.

Then consider m = l + (r - l >> 1), l = r - 1 and consider equal,
e.g., key == arr[m]. Suppose we have decided to return l instead of r, then
equal condition goes to the r = m branch.

```python
l, r = 0, len(arr) - 1
while l < r:
  m = l + (r - l >> 1)
  if in_left_half_condition:
    r = m
  else:
    l = m + 1
```
```python
l, r = 0, len(arr) - 1
while l < r:
  m = r - (r - l >> 1)
  if in_left_half_condition:
    r = m - 1
  else:
    l = m
```

## Types

1. ceiling/floor
2. half is sorted, find turning point

## Tricks

- skip repeated number first
