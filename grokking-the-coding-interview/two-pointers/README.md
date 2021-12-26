# Two Pointers

## Problems

1. [Comparing Strings containing Backspaces (medium)](Comparing-Strings-containing-Backspaces-(medium).py)
[[LC844](https://leetcode.com/problems/backspace-string-compare)]
1. [Dutch National Flag Problem (medium)](Dutch-National-Flag-Problem-(medium).py)
[[LC75](https://leetcode.com/problems/sort-colors)]
1. [Minimum Window Sort (medium)](Minimum-Window-Sort-(medium).py)
[[LC581](https://leetcode.com/problems/shortest-unsorted-continuous-subarray)]
1. [Pair with Target Sum (easy)](Pair-with-Target-Sum-(easy).py)
[[LC167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)]
1. [Quadruple Sum to Target (medium)](Quadruple-Sum-to-Target-(medium).py)
[[LC18](https://leetcode.com/problems/4sum)]
1. [Remove Duplicates (easy)](Remove-Duplicates-(easy).py)
[[LC26](https://leetcode.com/problems/remove-duplicates-from-sorted-array)]
1. [Remove Element (easy)](Remove-Element-(easy).py)
[[LC27](https://leetcode.com/problems/remove-element)]
1. [Squaring a Sorted Array (easy)](Squaring-a-Sorted-Array-(easy).py)
[[LC977](https://leetcode.com/problems/squares-of-a-sorted-array)]
1. [Subarrays with Product Less than a Target (medium)](Subarrays-with-Product-Less-than-a-Target-(medium).py)
[[LC713](https://leetcode.com/problems/subarray-product-less-than-k)]
1. [Triplet Sum Close to Target (medium)](Triplet-Sum-Close-to-Target-(medium).py)
[[LC16](https://leetcode.com/problems/3sum-closest)]
1. [Triplet Sum to Zero (medium)](Triplet-Sum-to-Zero-(medium).py)
[[LC15](https://leetcode.com/problems/3sum)]
1. [Triplets with Smaller Sum (medium)](Triplets-with-Smaller-Sum-(medium).py)
[[LC259](https://leetcode.com/problems/3sum-smaller)]

## Pattern

- sorted array
- compare two arrays
- in-place reconstruction of an array

## Pipeline

1. decide the start/end point
2. move pointers

## Types

1. k sum: deduce to 2 sum
2. in-place reconstruction: one ptr indicates the index to put new item,
   another ptr to iterate the array
3. find a sub-structure: sometimes similar to sliding window, can also shrink two pointers starting from both ends

## Tricks

- freedom of direction: pointers can go from left to right/right to left/center to ends/ends to center
