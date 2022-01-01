# Breadth First Search

## Problems

1. [Binary Tree Level Order Traversal (easy)](Binary-Tree-Level-Order-Traversal-(easy).py)
[[LC102](https://leetcode.com/problems/binary-tree-level-order-traversal/)]
1. [Reverse Level Order Traversal (easy)](Reverse-Level-Order-Traversal-(easy).py)
[[LC107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)]
1. [Zigzag Traversal (medium)](Zigzag-Traversal-(medium).py)
[[LC103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)]
1. [Level Averages in a Binary Tree (easy)](Level-Averages-in-a-Binary-Tree-(easy).py)
[[LC637](https://leetcode.com/problems/average-of-levels-in-binary-tree/)]
1. [Find Largest Value in Each Tree Row (medium)](Find-Largest-Value-in-Each-Tree-Row-(medium).py)
[[LC515](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)]
1. [Minimum Depth of a Binary Tree (easy)](Minimum-Depth-of-a-Binary-Tree-(easy).py)
[[LC111](https://leetcode.com/problems/minimum-depth-of-binary-tree/)]
1. [Maximum Depth of Binary Tree (easy)](Maximum-Depth-of-Binary-Tree-(easy).py)
[[LC104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)]
1. [Level Order Successor (easy)](Level-Order-Successor-(easy).py)
[[LC1602](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/)]
1. [Connect Level Order Siblings (medium)](Connect-Level-Order-Siblings-(medium).py)
[[LC117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)]
1. [Connect All Level Order Siblings (medium)](Connect-All-Level-Order-Siblings-(medium).py)
1. [Right View of a Binary Tree (easy)](Right-View-of-a-Binary-Tree-(easy).py)
[[LC199](https://leetcode.com/problems/binary-tree-right-side-view/)]
1. [Left View of a Binary Tree (easy)](Left-View-of-a-Binary-Tree-(easy).py)
[[link](https://www.techiedelight.com/print-left-view-of-binary-tree)]

## Pattern

- tree
- depth/level order
- connect siblings

## Pipeline

### traverse level by length
```python
from collections import deque


if not root:
	return None 
level = deque([root])
while level:
	l = len(level)  # size of a level
	# traverse a level
	for i in range(l):
		node = level.popleft()
		if i == 0:
			# the first in this level
		if i == l - 1:
			# the last in this level
		if node.left:
			level.append(node.left)
		if node.right:
			level.append(node.right)

```

### traverse next level in O(1) space with sibling pointer
```python
if not root:
	return None 
# `start` and `end` are two side nodes in the same level
start = root
end = root 
while start:
	it = iter_next_level(start)
	left_sibling = next(it, None)
	next_level_start = left_sibling

	right_sibling = None
	for right_sibling in it:
		left_sibling.next = right_sibling
		left_sibling = right_sibling
	# `right_sibling` becomes the end ndoe in the next level
	end.next = next_level_start  # `next_end` is at the same level as `start`

	start, end = next_level_start, right_sibling

	return root


def iter_next_level(node):
	# node is the start of a level
	while node:
		if node.left:
			yield node.left
		if node.right:
			yield node.right
		node = node.next
```

## Types

1. traversal order by depth: count depth
1. smallest/largest depth: count depth
1. level statistics: keep level nodes
1. siblings: use iterator

## Tricks

- use iterator for sibling traversal

## Resources 

- [tree views and traversal](https://leetcode.com/discuss/general-discussion/1094690/views-and-traversal-of-binary-tree-important-topics-must-read)
