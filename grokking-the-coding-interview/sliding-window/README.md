# Sliding Window

## Problems

1. [Maximum Sum Subarray of Size K (easy)](Maximum-Sum-Subarray-of-Size-K-(easy).py)
2. [Smallest Subarray with a given sum (easy)](Smallest-Subarray-with-a-given-sum-(easy).py)
2. [Longest Substring with maximum K Distinct Characters (medium)](Longest-Substring-with-maximum-K-Distinct-Characters-(medium).py)
2. [Fruits into Baskets (medium)](Fruits-into-Baskets-(medium).py)
2. [Longest Substring with Distinct Characters (hard)](Longest-Substring-with-Distinct-Characters-(hard).py)
2. [Longest Substring with Same Letters after Replacement (hard)](Longest-Substring-with-Same-Letters-after-Replacement-(hard).py)
2. [Longest Subarray with Ones after Replacement (hard)](Longest-Subarray-with-Ones-after-Replacement-(hard).py)
2. [Permutation in a String (hard)](Permutation-in-a-String-(hard).py)
2. [String Anagrams (hard)](String-Anagrams-(hard).py)
2. [Smallest Window containing Substring-(hard)](Smallest-Window-containing-Substring-(hard).py)
2. [Words Concatenation (hard)](Words-Concatenation-(hard).py)

## Pattern

- continuous
- sub-array, -string

## Pipeline

1. Expand: iterate `window_end` 
2. Shrink: when meeting some conditions, increase `window_start`

```python
win_start = 0
best_window_size = 0  # or inf

for window_end, element in enumerate(arr):
    # do something with element
    while condition:
        # update best_window_size
        ...
        window_start += 1
```

## Tricks

- use dict 
  - char to index
  - char to frequency
    - use a variable to represent the sum of **non-negative** frequencies appeared within the window
- use `if` instead of `while`
  - when only need to keep track of the largest ever windows
