# Fast and Slow Pointers

## Pattern

- linked list
- cycle 
- half of linked list

## Pipeline

```python
slow, fast = head, head 
while head is not None and head.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        # slow is a node within the cycle
# no cycle
```

## Types

- exist cycle: `slow` moves by 1, `fast` by 2
- middle node: after breaking while, `slow` is the middle or second middle point
- left and right half: first reverse the right half and start from the right end

## Tricks

- can use `if slow sis not fast:`
