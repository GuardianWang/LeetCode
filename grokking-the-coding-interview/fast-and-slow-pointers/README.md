# Fast and Slow Pointers

## Problems

1. [Cycle in a Circular Array (hard)](Cycle-in-a-Circular-Array-(hard).py)
[[LC457]()]

1. [Happy Number (medium)](Happy-Number-(medium).py)
[[LC202]()]

1. [LinkedList Cycle (easy)](LinkedList-Cycle-(easy).py)
[[LC141]()]

1. [LinkedList Cycle Length (easy)](LinkedList-Cycle-Length-(easy).py)

1. [Middle of the LinkedList (easy)](Middle-of-the-LinkedList-(easy).py)
[[LC](876)]

1. [Palindrome LinkedList (medium)](Palindrome-LinkedList-(medium).py)
[[LC](234)]

1. [Rearrange a LinkedList (medium)](Rearrange-a-LinkedList-(medium).py)
[[LC](143)]

1. [Start of LinkedList Cycle (medium)](Start-of-LinkedList-Cycle-(medium).py)
[[LC](142)]

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

- cycle: existence, length, start
- middle node: after breaking while, `slow` is the middle or second middle point
- left and right half: first reverse the right half and start from the right end

## Tricks

- can use `if slow sis not fast:`
- slow fast pointers first find a point within the cycle, then count the length of the cycle,
  then start from head and find the start of the cycle
