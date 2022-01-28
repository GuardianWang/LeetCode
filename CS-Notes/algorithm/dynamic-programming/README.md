# Dynamic Programming

## Problems

1. [Climbing Stairs (Easy)]()
[[LC70](https://leetcode.com/problems/climbing-stairs/description/)]
1. [House Robber (Medium)]()
[[LC198](https://leetcode.com/problems/house-robber/description/)]
1. [House Robber II (Medium)]()
[[LC213](https://leetcode.com/problems/house-robber-ii/description/)]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]
1. []()
[[LC]()]

## Pipeline

## Tricks

- `if n & 1`: odd

### O(logN) power of N
```python
def pow(a, n):
  remain = 1
  power = 1
  while power <= n:
    # a is input_a ^ power
    if power & n:
      remain *= a
    a *= a
    power >>= 1
  return a
```
