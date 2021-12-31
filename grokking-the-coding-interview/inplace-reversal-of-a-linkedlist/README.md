# In-place Reversal of a LinkedList

## Problems

1. [Reverse a LinkedList (easy)](Reverse-a-LinkedList-(easy).py)
[[LC206](https://leetcode.com/problems/reverse-linked-list/)]
1. [Reverse a Sub-list (medium)](Reverse-a-Sub-list-(medium).py)
[[LC92](https://leetcode.com/problems/reverse-linked-list-ii/submissions/)]
1. [Reverse first k elements (easy)](Reverse-first-k-elements-(easy).py)
1. [Reverse by size (medium)](Reverse-by-size-(medium).py)
1. [Reverse every K-element Sub-list (medium)](Reverse-every-K-element-Sub-list-(medium).py)
[[LC25](https://leetcode.com/problems/reverse-nodes-in-k-group/)]
1. [Reverse alternating K-element Sub-list (medium)](Reverse-alternating-K-element-Sub-list-(medium).py)
1. [Rotate a LinkedList (medium)](Rotate-a-LinkedList-(medium).py)
[[LC61](https://leetcode.com/problems/rotate-list/)]

## Pattern

- reverse a linked list

## Pipeline

### naive reverse
```python
left, mid = None, head
while mid:
  right = mid.next
  mid.next = left
  left, mid = mid, right
# now left becomes the last non-None node
```

### reverse a sub-list
```python
# given head, l, r
# reverse indices within [l, r]
# l, r are 1-indexed
sent = Node(None, head)  # sentinel
prev = sent
for _ in range(l - 1):
  prev = prev.next
# prev is the node before node at index l
l_node = prev.next

# similar to reverse the whole
left, mid = prev, l_node
for _ in range(r - l + 1):
  right = mid.next
  mid.next = left
  left, mid = mid, right
# now left becomes the node at index r in the original list
prev.next = left
l_node.next = mid
# now l_node becomes the node at index r in the new list
```

### length
```python
cnt = 0
while head:
  head = head.next
  cnt += 1
# cnt is the length
```

## Types

1. reverse the whole list
2. reverse a sub-list
3. rotate: rotate k to the right, then the first `len - k` nodes remain the same
