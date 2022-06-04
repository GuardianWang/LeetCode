# Sliding Window

## Problems

1. [Maximum Sum Subarray of Size K (easy)](Maximum-Sum-Subarray-of-Size-K-(easy).py)
2. [Smallest Subarray with a given sum (easy)](Smallest-Subarray-with-a-given-sum-(easy).py)
[[LC209](https://leetcode.com/problems/minimum-size-subarray-sum)]
3. [Longest Substring with maximum K Distinct Characters (medium)](Longest-Substring-with-maximum-K-Distinct-Characters-(medium).py)
[[LC340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters)]
4. [Fruits into Baskets (medium)](Fruits-into-Baskets-(medium).py)
[[LC904](https://leetcode.com/problems/fruit-into-baskets)]
2. [Longest Substring with Distinct Characters (hard)](Longest-Substring-with-Distinct-Characters-(hard).py)
[[LC3](https://leetcode.com/problems/longest-substring-without-repeating-characters)]
2. [Longest Substring with Same Letters after Replacement (hard)](Longest-Substring-with-Same-Letters-after-Replacement-(hard).py)
[[LC424](https://leetcode.com/problems/longest-repeating-character-replacement)]
2. [Longest Subarray with Ones after Replacement (hard)](Longest-Subarray-with-Ones-after-Replacement-(hard).py)
[[LC1004](https://leetcode.com/problems/max-consecutive-ones-iii)]
2. [Permutation in a String (hard)](Permutation-in-a-String-(hard).py)
[[LC567](https://leetcode.com/problems/permutation-in-string)]
2. [String Anagrams (hard)](String-Anagrams-(hard).py)
[[LC438](https://leetcode.com/problems/find-all-anagrams-in-a-string)]
2. [Smallest Window containing Substring-(hard)](Smallest-Window-containing-Substring-(hard).py)
[[LC76](https://leetcode.com/problems/minimum-window-substring)]
2. [Words Concatenation (hard)](Words-Concatenation-(hard).py)
[[LC30](https://leetcode.com/problems/substring-with-concatenation-of-all-words)]

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

### permutation
```python
pattern_freq =  # dict
pattern_char_set =  # dict 
l = 0
def add_char(char):
    if char not in pattern_char_set:
        return
    pattern_freq[c] += 1
    if not pattern_freq[c]:
        del pattern_freq[c]

def rm_char(char):
    if char not in pattern_char_set:
        return
    pattern_freq[c] -= 1
    if not pattern_freq[c]:
        del pattern_freq[c]

l = 0
for r, char in enumerate(string):
    rm_char(char)
    if not char:
        # current window is a permutation of pattern
    if r >- len(pattern) - 1:
        add_char(string[l])
        l += 1

```

## Tricks

- use dict 
  - char to index
  - char to frequency
    - use a variable to represent the sum of **non-negative** frequencies appeared within the window
- use `if` instead of `while`
  - when only need to keep track of the largest ever windows
