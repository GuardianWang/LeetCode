# Sliding Window

## Problems

1. 

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
